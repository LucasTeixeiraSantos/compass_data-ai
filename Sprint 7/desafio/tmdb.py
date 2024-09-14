import requests

url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzI2YWIwNmM5MDBiMTMyMjU2ODE4YTIzZTU5YTBlYSIsIm5iZiI6MTcyNTAzODA5OC42MTMwODQsInN1YiI6IjY2ZDFmNmU5NmU5Nzk1M2IwNTk0M2EwMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TL6x5qI7oM3-LGsx_ih83FYerpKiFcki-iWglTxwnOs"
}

response = requests.get(url, headers=headers)

print(response.text)