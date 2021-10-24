import tmdbsimple as tmdb
import requests


class TmdbCliCommand:
    """This class aims to initialize cli command properly
    It takes args in parameters and a Tmdb api session.
    """

    def __init__(self, args) -> None:
        args = self.args
        self.tmdb_session = self._get_tmdb_session()

    def _get_tmdb_session(self):
        try:
            tmdb.API_KEY = "2f43b8eb90c3e33d14e3fda48df3fa5"
            tmdb.REQUESTS_SESSION = requests.Session()
            return tmdb
        except Exception:
            print("Could not connect to api")

    def tmdb_search(self):
        try:
            search = self.tmdb_session.Search()
            return search
        except: 
            print("Could not connect to api")

    
    def tmdb_discover(self):
        try:
            discover = self.tmdb_session.Discover()
            return discover

        except: 
            print("Could not connect to api")

