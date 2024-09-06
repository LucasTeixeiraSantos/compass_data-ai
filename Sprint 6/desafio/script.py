import boto3
import os
from datetime import datetime
from tqdm import tqdm


def verify_or_create_bucket(bucket_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except:
        s3_client.create_bucket(Bucket=bucket_name)

def iterate_folder_and_upload_to_s3(bucket_name, data_directory):
    for file_name in os.listdir(data_directory):
        if file_name.endswith(".csv"):
            file_path = os.path.join(data_directory, file_name)
            upload_to_s3(file_path, file_name, bucket_name)  
            
def upload_to_s3(file_path, file_name, bucket_name):
    s3_client = boto3.client('s3')
    date_path = datetime.today().strftime('%Y/%m/%d')
    file_name_upper_no_ext = os.path.splitext(file_name)[0].capitalize()
    file_extension = os.path.splitext(file_name)[1][1:].upper()
    s3_path = f"Raw/Local/{file_extension}/{file_name_upper_no_ext}/{date_path}/{file_name}"
    file_size = os.path.getsize(file_path)
    with open(file_path, 'rb') as f:
        with tqdm(total=file_size, unit='B', unit_scale=True, desc=file_name) as pbar:
            s3_client.upload_fileobj(f, bucket_name, s3_path, Callback=lambda bytes_transferred: pbar.update(bytes_transferred))

    print(f"UPLOAD: {file_name} on BUCKET: s3://{bucket_name}/{s3_path} was successful.")
 
def main():
    bucket_name = "teste-bucket-luc"
    data_directory = "C:/Users/lucas/Desktop/Projetos/compass_data-ai/Sprint 6/desafio/data"

    verify_or_create_bucket(bucket_name)
    iterate_folder_and_upload_to_s3(bucket_name, data_directory)

if __name__ == "__main__":
    main()