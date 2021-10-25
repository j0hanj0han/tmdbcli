"""
This file represents the CastingFinderCommand class used for the TMDB Cli with the castingfinder command.
The aim of this class is to find films where two or more actors played together.
"""
from typing import List


class CastingFinderCommand:
    def __init__(self, actors_list, api_client):
        """
        This class aims to retrieve movies where actors passed in parameters played together
        Parameters: a string of actors list separated by commas and the api client for TMDB API.
        """
        self.api_client = api_client
        self.actors = actors_list.split(",")

    def _find_actor_ids(self, actors_list):
        """
        This function aims to retrieve actors ids from a names list.
        Parameters: actors list.
        Return a list of actor ids.
        """
        actor_ids = []
        for actor in actors_list:
            print(f"TMDB API: Trying to find actor '{actor}' ...")
            query = f"{actor}"
            results = self.api_client.tmdb_search_person(query=query)["results"]
            # If there's multiple actor names, it returns the first id and name from the results.
            # It could be improved for a future version of the CLI.
            if len(results) != 0:
                actor_id = results[0]["id"]
                actor_name = results[0]["name"]
                print(f"TMDB API: Found id for {actor_name}: {actor_id}")
                actor_ids.append(actor_id)
            else:
                print(f"TMDB API: Could not find {actor}")
        return actor_ids

    def find_movies(self):
        """Returns a list of movies names where actors id are present"""
        query = f"{','.join(str(id) for id in self._find_actor_ids(self.actors))}"
        raw_result = self.api_client.tmdb_discover_movie_with_cast(query)["results"]
        movies = [movie["original_title"] for movie in raw_result]
        return movies
