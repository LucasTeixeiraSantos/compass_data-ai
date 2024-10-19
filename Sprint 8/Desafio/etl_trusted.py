import sys
import boto3
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import trim, col, when, to_date, lower, lit
from pyspark.sql.types import StringType

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session
job = Job(glueContext)

RAW_JSON_PATH = "s3://data-lake-lucas-ts/Raw/TMDB/JSON/"
RAW_CSV_PATH = "s3://data-lake-lucas-ts/Raw/Local/CSV/Movies/"
TRUSTED_OUTPUT_PATH = "s3://data-lake-lucas-ts/Trusted/PARQUET/"

def list_s3_files(path):
    s3_client = boto3.client('s3')
    bucket = path.split('/')[2]
    prefix = '/'.join(path.split('/')[3:])
    
    result = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    return [
        f"s3://{bucket}/{obj['Key']}" 
        for obj in result.get('Contents', []) 
        if obj['Key'].endswith(('json', 'csv'))
    ]

def read_and_union_files(file_paths, file_type):
    union_df = None
    for file in file_paths:
        df = spark.read.json(file) if file_type == 'json' else spark.read.csv(file, sep='|', header=True, inferSchema=True)
        union_df = df if union_df is None else union_df.union(df)
    return union_df

def trim_dataframe(df):
    for field in df.schema.fields:
        if isinstance(field.dataType, StringType):
            df = df.withColumn(field.name, trim(col(field.name)))
    return df

def replace_nulls(df):
    for column in df.columns:
        df = df.withColumn(
            column, 
            when((col(column) == r"\N") | (col(column) == ""), None).otherwise(col(column))
        )
    return df

json_files = list_s3_files(RAW_JSON_PATH)
csv_files = list_s3_files(RAW_CSV_PATH)

movies_json_df = read_and_union_files(json_files, 'json')
movies_csv_df = read_and_union_files(csv_files, 'csv')

movies_json_df = trim_dataframe(movies_json_df)
movies_csv_df = trim_dataframe(movies_csv_df)

movies_csv_df = movies_csv_df.withColumnRenamed("id", "imdb_id")

result_df = movies_json_df.join(movies_csv_df, on='imdb_id', how='left')

result_df = result_df.select(
    col('anoFalecimento').cast('int').alias('artist_death_year'),
    col('anoNascimento').cast('int').alias('artist_birth_year'),
    col('backdrop_path').cast('string').alias('path_backdrop'),
    lower(col('generoArtista')).cast('string').alias('artist_gender'),
    col('id').cast('string').alias('id_tmdb'),
    col('imdb_id').cast('string').alias('id_imdb'),
    col('nomeArtista').cast('string').alias('artist_name'),
    col('notaMedia').cast('double').alias('vote_average_imdb'),
    col('numeroVotos').cast('int').alias('vote_count_imdb'),
    col('original_title').cast('string').alias('title_original'),
    col('overview').cast('string').alias('overview'),
    col('personagem').cast('string').alias('artist_character'),
    col('poster_path').cast('string').alias('path_poster'),
    col('profissao').cast('string').alias('artist_profession'),
    to_date(col('release_date'), 'yyyy-MM-dd').alias('release_date'),
    col('revenue').cast('bigint').alias('revenue'),
    col('runtime').cast('int').alias('runtime'),
    col('tagline').cast('string').alias('tagline'),
    col('title').cast('string').alias('title'),
    col('vote_average').cast('double').alias('vote_average_tmdb'),
    col('vote_count').cast('int').alias('vote_count_tmdb'),
    col('budget').cast('bigint').alias('budget')
)

result_df = replace_nulls(result_df)

result_df = result_df.orderBy(col('vote_count_tmdb').desc())

current_date = datetime.now()
result_df = result_df.withColumn("year", lit(current_date.year)) \
                     .withColumn("month", lit(current_date.month)) \
                     .withColumn("day", lit(current_date.day))

result_df.write.mode("overwrite") \
    .partitionBy("year", "month", "day") \
    .parquet(TRUSTED_OUTPUT_PATH)

job.commit()