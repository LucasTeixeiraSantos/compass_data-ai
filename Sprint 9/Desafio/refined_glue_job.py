import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from pyspark.sql import SQLContext, Row
from pyspark.sql.functions import monotonically_increasing_id, col, min, max, sequence, explode, lit, to_date, expr
from pyspark.sql.types import DateType
from datetime import timedelta


sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
sqlContext = SQLContext(sc)

TRUSTED_INPUT_PATH = "s3://data-lake-lucas-ts/Trusted/PARQUET/"
REFINED_OUTPUT_PATH = "s3://data-lake-lucas-ts/Refined/PARQUET/"

trusted_df = spark.read.parquet(TRUSTED_INPUT_PATH)

dim_artist = trusted_df.select(
    "artist_name",
    "artist_gender",
    "artist_birth_year",
    "artist_death_year",
    "artist_profession",
).dropDuplicates(["artist_name"])

dim_artist = dim_artist.withColumn("id_artist_name", monotonically_increasing_id())

dim_movie = trusted_df.select(
    "title", "path_backdrop", "title_original", "overview", "path_poster", "tagline"
).dropDuplicates(["title"])

dim_movie = dim_movie.withColumn("id_movie", monotonically_increasing_id())

dim_character = trusted_df.select("artist_character").dropDuplicates(
    ["artist_character"]
)

dim_character = dim_character.withColumn("id_character", monotonically_increasing_id())
fact_movies = trusted_df.select(
    "id_tmdb",
    "id_imdb",
    "vote_average_imdb",
    "vote_count_imdb",
    "revenue",
    "runtime",
    "vote_average_tmdb",
    "vote_count_tmdb",
    "budget",
    "title",
    "artist_name",
    "artist_character",
    "release_date",
)

fact_movies = (
    fact_movies.join(dim_movie, fact_movies["title"] == dim_movie["title"], "left")
    .join(dim_artist, fact_movies["artist_name"] == dim_artist["artist_name"], "left")
    .join(
        dim_character,
        fact_movies["artist_character"] == dim_character["artist_character"],
        "left",
    )
    .select(
        fact_movies["id_tmdb"],
        fact_movies["id_imdb"],
        fact_movies["vote_average_imdb"],
        fact_movies["vote_count_imdb"],
        fact_movies["release_date"],
        fact_movies["revenue"],
        fact_movies["runtime"],
        fact_movies["vote_average_tmdb"],
        fact_movies["vote_count_tmdb"],
        fact_movies["budget"],
        dim_movie["id_movie"],
        dim_artist["id_artist_name"],
        dim_character["id_character"],
    )
)

min_date = fact_movies.agg(min("release_date")).collect()[0][0]
max_date = fact_movies.agg(max("release_date")).collect()[0][0]

calendar_df = spark.sql(
    """
    SELECT sequence(to_date('{0}'), to_date('{1}'), interval 1 day) AS date_range
""".format(
        min_date, max_date
    )
)

dim_calendar = (
    calendar_df.selectExpr("explode(date_range) AS date")
    .withColumn("year", expr("year(date)"))
    .withColumn("month", expr("month(date)"))
    .withColumn("day", expr("day(date)"))
)

dim_artist.write.mode("overwrite").parquet(f"{REFINED_OUTPUT_PATH}/dim_artist")
dim_movie.write.mode("overwrite").parquet(f"{REFINED_OUTPUT_PATH}/dim_movie")
dim_character.write.mode("overwrite").parquet(f"{REFINED_OUTPUT_PATH}/dim_character")
fact_movies.write.mode("overwrite").parquet(f"{REFINED_OUTPUT_PATH}/fact_movies")
dim_calendar.write.mode("overwrite").parquet(f"{REFINED_OUTPUT_PATH}/dim_calendar")

print("Modeling completed and data saved in the Refined layer!")

spark.stop()
sc.stop()
