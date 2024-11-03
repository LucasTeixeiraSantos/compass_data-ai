import json
import aiohttp
import asyncio
import boto3
import os
from botocore.exceptions import ClientError
from datetime import datetime, timezone

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
S3_BUCKET = "data-lake-lucas-ts"

BASE_URL_DISCOVER = "https://api.themoviedb.org/3/discover/movie"
BASE_URL_MOVIE = "https://api.themoviedb.org/3/movie"
HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB_API_KEY}"
}
PARAMS = {
    "with_companies": "10342",
    "sort_by": "popularity.desc"
}

s3 = boto3.client('s3')

async def get_movies_from_api(session, page):
    params = {**PARAMS, "page": page}
    async with session.get(BASE_URL_DISCOVER, headers=HEADERS, params=params) as response:
        if response.status == 200:
            data = await response.json()
            return data.get('results', []), data.get('total_pages', 1)
        if response.status == 429:
            await asyncio.sleep(1)
            return await get_movies_from_api(session, page)
        response.raise_for_status()

async def get_movie_details(session, movie_id):
    async with session.get(f"{BASE_URL_MOVIE}/{movie_id}?sort_by=popularity.desc", headers=HEADERS) as response:
        if response.status == 200:
            return await response.json()
        if response.status == 429:
            await asyncio.sleep(1)
            return await get_movie_details(session, movie_id)
        response.raise_for_status()

def save_to_s3(data, file_name):
    now = datetime.now(timezone.utc)
    s3_key = f"Raw/TMDB/JSON/{now:%Y/%m/%d}/{file_name}"
    try:
        s3.put_object(
            Bucket=S3_BUCKET,
            Key=s3_key,
            Body=json.dumps(data, ensure_ascii=False),  
            ContentType='application/json'
        )
        print(f"File saved at: {s3_key}")
    except ClientError as e:
        print(f"Failed to save file: {e}")
        raise

async def fetch_all_movie_details(session, movie_ids):
    tasks = [get_movie_details(session, movie_id) for movie_id in movie_ids]
    return await asyncio.gather(*tasks)

async def fetch_and_save_movies():
    async with aiohttp.ClientSession() as session:
        movies, total_pages = await get_movies_from_api(session, 1)
        
        movie_ids = [movie['id'] for movie in movies]  
        
        if total_pages > 1:
            for page in range(2, total_pages + 1):
                movies, _ = await get_movies_from_api(session, page)
                movie_ids.extend(movie['id'] for movie in movies)
        
        movie_details = await fetch_all_movie_details(session, movie_ids)
        
        file_name = f"movies_details.json"
        save_to_s3(movie_details, file_name)

def main():
    asyncio.run(fetch_and_save_movies())

if __name__ == "__main__":
    main()
