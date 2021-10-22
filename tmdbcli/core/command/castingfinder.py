import tmdbsimple as tmdb
import requests
import os

def connect_to_api():
    try:
        tmdb.API_KEY = 
        tmdb.REQUESTS_SESSION = requests.Session()
    except Exception as e:
        print(e)


class CastingFinderCommand():

    '''This Class take 2 actors in parameters
       It returns a list of movies where two actors played together
    '''

    def __init__(self, actor1, actor2) -> None:
        self.connect_to_db = connect_to_api()
        self.actors = [actor1, actor2]
        
    def is_people_actor():
        return true

    def _find_people_id(self):
        '''
        This functions aims to retrieve TMDB people'id passed in parameters during the initialization of the CastingFinderCommand
        return people id from tmdb in a dictionnary
        '''
        self.people_ids = {}
        for actor in self.actors:
            print(f"Trying to find people {actor} in TMDB")
            search = tmdb.Search()
            # attach the real name
            actor_id = search.person(query=f"{actor}")["results"][0]["id"]
            # take the first
            print(f"Found id for {actor}: {actor_id}")
            self.people_ids[f"{actor}"] = actor_id
        print(self.people_ids)
        return self.people_ids


    def _sanitize_people(self):
        '''
        This functions aims to sanitize the name we put on it lower case or not
        '''
        pass

    def compute(self):
        
        ids_formatted_for_query = ",".join(str(id) for id in list(self.people_ids.values()))
        actor_formatted_for_results = ','.join(actor for actor in list(self.people_ids.keys()))
        query = tmdb.Discover().movie(with_cast=ids_formatted_for_query)
        print(f"Found {query['total_results'] } films, with {actor_formatted_for_results}")
        for r in query["results"]:
            print(r["original_title"])


def helloworld():
    casting_finder_command = CastingFinderCommand('brad pitt', 'angelina jolie')
    casting_finder_command._find_people_id()
    casting_finder_command.compute()
