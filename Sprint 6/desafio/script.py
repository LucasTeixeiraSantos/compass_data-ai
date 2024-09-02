import boto3
import os
from datetime import datetime
from botocore.exceptions import NoCredentialsError, ClientError

def create_bucket_if_not_exists(bucket_name, region=None):
    s3_client = boto3.client('s3')
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} already exists.")
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            print(f"Bucket {bucket_name} does not exist. Creating bucket...")
            if region is None or region == 'us-east-1':
                s3_client.create_bucket(Bucket=bucket_name)
            else:
                s3_client.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': region}
                )
            print(f"Bucket {bucket_name} created successfully.")
        else:
            print(f"Error trying to verify the bucket: {e}")

def upload_to_s3(file_name, bucket, storage_layer, data_source, data_format, data_spec):
    s3_client = boto3.client('s3')
    
    today = datetime.today()
    date_path = today.strftime('%Y/%m/%d')
    
    s3_path = f"{storage_layer}/{data_source}/{data_format}/{data_spec}/{date_path}/{os.path.basename(file_name)}"
    
    try:
        s3_client.upload_file(file_name, bucket, s3_path)
        print(f"UPLOAD: {file_name} on BUCKET:  {bucket} at PATH: {s3_path} was succesfull.")
    except NoCredentialsError:
        print("Erro: Credentials not found.")
    except ClientError as e:
        print(f"Error trying to upload file into the S3: {e}")

def main():
    bucket_name = "data-lake-lucas-ts"
    region = "us-east-1"

    create_bucket_if_not_exists(bucket_name, region)
    
    storage_layer = "Raw"
    data_source = "Local"
    data_format = "CSV"

    data_directory = "/app/data"

    for file_name in os.listdir(data_directory):
        if file_name.endswith(".csv"):
            full_file_path = os.path.join(data_directory, file_name)
            data_spec = os.path.splitext(file_name)[0].capitalize()
            upload_to_s3(full_file_path, bucket_name, storage_layer, data_source, data_format, data_spec)

if __name__ == "__main__":
    main()
