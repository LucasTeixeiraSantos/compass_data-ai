import json
import aiohttp
import asyncio
import boto3
import os
from botocore.exceptions import ClientError
from datetime import datetime, timezone

TMDB_API_KEY = os.environ.get('TMDB_API_KEY')  
S3_BUCKET = os.environ.get('S3_BUCKET')
TMDB_TYPE = os.environ.get('TMDB_TYPE')
GENRE_ID = os.environ.get('GENRE_ID')

BASE_URL = f"https://api.themoviedb.org/3/discover/{TMDB_TYPE}"
HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB_API_KEY}"
}
PARAMS = {
    "language": "en-US",
    "sort_by": "popularity.desc",
    "with_genres": GENRE_ID,
    "vote_count.gte": "5"
}

s3 = boto3.client('s3')

async def get_movies_from_api(session, page):
    params = {**PARAMS, "page": page}
    async with session.get(BASE_URL, headers=HEADERS, params=params) as response:
        if response.status == 200:
            data = await response.json()
            return data.get('results', []), data.get('total_pages', 1)
        if response.status == 429:
            await asyncio.sleep(1)
            return await get_movies_from_api(session, page)
        response.raise_for_status()

def save_to_s3(data, file_name):
    now = datetime.now(timezone.utc)
    s3_key = f"Raw/TMDB/JSON/{now:%Y/%m/%d}/{file_name}"
    try:
        s3.put_object(
            Bucket=S3_BUCKET,
            Key=s3_key,
            Body=json.dumps(data),
            ContentType='application/json'
        )
        print(f"File saved at: {s3_key}")
    except ClientError as e:
        print(f"Failed to save file: {e}")
        raise

async def fetch_all_pages(session, total_pages):
    tasks = [get_movies_from_api(session, page) for page in range(1, total_pages + 1)]
    results = await asyncio.gather(*tasks)
    return results

async def fetch_and_save_movies():
    movie_data, file_count = [], 1

    async with aiohttp.ClientSession() as session:
        movies, total_pages = await get_movies_from_api(session, 1)

        if total_pages > 1:
            results = await fetch_all_pages(session, total_pages)

            for movies_batch, _ in results:
                movie_data.extend(movies_batch)

                while len(movie_data) >= 100:
                    file_name = f"movies_part_{str(file_count).zfill(3)}.json"
                    save_to_s3(movie_data[:100], file_name)
                    movie_data = movie_data[100:]
                    file_count += 1

        if movie_data:
            file_name = f"movies_part_{str(file_count).zfill(3)}.json"
            save_to_s3(movie_data, file_name)

async def async_handler(event, context):
    await fetch_and_save_movies()
    return {
        "statusCode": 200,
        "body": json.dumps("Done")
    }

def lambda_handler(event, context):
    return asyncio.run(async_handler(event, context))
