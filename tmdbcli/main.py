import tmdbsimple as tmdb
import requests
import os

tmdb.API_KEY = 
tmdb.REQUESTS_SESSION = requests.Session()


search = tmdb.Search()
response = search.movie(query='Matrix')
for s in search.results:
    print(s['title'], s['id'], s['release_date'], s['popularity'])


t = tmdb.discover(with_cast="1,2")

actor = tmdb.People(1).info()


# if __name__ == "__main__":
#     pass