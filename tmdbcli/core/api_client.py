import requests
import os
import tmdbsimple as tmdb

from tmdbcli.utils.errors import (
    TmdbSessionException,
    DiscoverException,
    SearchException,
)


class ApiClient:
    """This class aims is the client for the API TMDB"""

    def __init__(self):
        self.tmdb_session = self._get_tmdb_session()

    def _get_tmdb_session(self):
        try:
            tmdb.API_KEY = os.environ["API_KEY"]
            tmdb.REQUESTS_SESSION = requests.Session()
            return tmdb
        except TmdbSessionException:
            raise TmdbSessionException()

    def tmdb_search_person(self, query):
        try:
            search = self.tmdb_session.Search().person(query=query)
            return search
        except SearchException:
            raise SearchException()

    def tmdb_discover_movie_with_cast(self, query):
        try:
            discover = self.tmdb_session.Discover().movie(with_cast=query)
            return discover
        except DiscoverException:
            raise DiscoverException()
