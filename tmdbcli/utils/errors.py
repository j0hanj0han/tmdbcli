'''
This file aims to provide custom exceptions for TMDB cli package
'''


class ApiKeyNotFound(Exception):
    """Custom Message for Missing Api Key"""

    def __init__(self, message="API_KEY variable not found in os.environ, please provide it"):
        self.message = message
        super().__init__(self.message)
    

class TmdbSessionException(Exception):
    """Custom Message for Missing Api Key"""

    def __init__(self, message="TMDB API Error: Could not set a TMDB."):
        self.message = message
        super().__init__(self.message)


class DiscoverException(Exception):
    """Custom Message for failing in Discover Function"""

    def __init__(self, message="TMDB API Error: Could not make a call to Discover endpoint."):
        self.message=message
        super().__init__(self.message)

class SearchException(Exception):
    """Custom Message for failing in Search Function"""

    def __init__(self, message="TMDB API Error: Could not make a call to Search endpoint."):
        self.message=message
        super().__init__(self.message)