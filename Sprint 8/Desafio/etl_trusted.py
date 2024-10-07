import sys
import boto3
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession
from pyspark.sql.functions import trim, col, when, to_date, lower
from pyspark.sql.types import StringType

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session
job = Job(glueContext)

JSON_PATH = "s3://data-lake-lucas-ts/Raw/TMDB/JSON/"
CSV_PATH = "s3://data-lake-lucas-ts/Raw/Local/CSV/Movies/"
OUTPUT_PATH = "s3://data-lake-lucas-ts/Trusted/PARQUET/{year}/{month}/{day}/"

def list_s3_files(bucket_prefix):
    s3_client = boto3.client('s3')
    bucket = bucket_prefix.split('/')[2]
    prefix = '/'.join(bucket_prefix.split('/')[3:])
    
    result = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    files = ["s3://{}/{}".format(bucket, obj['Key']) for obj in result.get('Contents', []) if obj['Key'].endswith(('json', 'csv'))]
    
    return files

def read_and_union_files(file_paths, file_type):
    union_df = None
    for file in file_paths:
        if file_type == 'json':
            df = spark.read.json(file)
        elif file_type == 'csv':
            df = spark.read.csv(file, sep='|', header=True, inferSchema=True)
        
        if union_df is None:
            union_df = df
        else:
            union_df = union_df.union(df)
    
    return union_df

def clean_dataframe(df):
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

json_files = list_s3_files(JSON_PATH)
movies_details_df = read_and_union_files(json_files, 'json')

csv_files = list_s3_files(CSV_PATH)
movies_csv_df = read_and_union_files(csv_files, 'csv')

movies_details_df = clean_dataframe(movies_details_df)
movies_csv_df = clean_dataframe(movies_csv_df)

movies_csv_df = movies_csv_df.withColumnRenamed("id", "imdb_id")

result_df = movies_details_df.join(movies_csv_df, on='imdb_id', how='left')

result_df = result_df.select(
    trim(col('anoFalecimento')).cast('int').alias('artist_death_year'),
    trim(col('anoNascimento')).cast('int').alias('artist_birth_year'),
    trim(col('backdrop_path')).alias('path_backdrop'),
    lower(trim(col('generoArtista'))).alias('artist_gender'),
    trim(col('id')).alias('id_tmdb'),
    trim(col('imdb_id')).alias('id_imdb'),
    trim(col('nomeArtista')).alias('artist_name'),
    trim(col('notaMedia')).cast('double').alias('vote_average_imdb'),
    trim(col('numeroVotos')).cast('int').alias('vote_count_imdb'),
    trim(col('original_title')).alias('title_original'),
    trim(col('overview')).alias('overview'),
    trim(col('personagem')).alias('artist_character'),
    trim(col('poster_path')).alias('path_poster'),
    trim(col('profissao')).alias('artist_profession'),
    to_date(trim(col('release_date')), 'yyyy-MM-dd').alias('release_date'),
    trim(col('revenue')).cast('bigint').alias('revenue'),
    trim(col('runtime')).cast('int').alias('runtime'),
    trim(col('tagline')).alias('tagline'),
    trim(col('title')).alias('title'),
    trim(col('vote_average')).cast('double').alias('vote_average_tmdb'),
    trim(col('vote_count')).cast('int').alias('vote_count_tmdb'),
    trim(col('budget')).cast('bigint').alias('budget')
)

result_df = replace_nulls(result_df)
result_df = result_df.orderBy(col('vote_count_tmdb').desc())

current_date = datetime.now()
year, month, day = current_date.year, current_date.month, current_date.day
parquet_output_path = OUTPUT_PATH.format(year=year, month=month, day=day)

result_df.write.mode("overwrite").parquet(parquet_output_path)

job.commit()
