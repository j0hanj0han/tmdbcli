"""
This file represents the CastingFinderCommand class used for the TMDB Cli with the withcast.
The aim of this class is to find films where two or more actors played together.
"""

from typing import List
from tmdbcli.core.command.command import TmdbCliCommand


class CastingFinderCommand(TmdbCliCommand):

    """This class take a list of actors in parameters.
    The list must contain at least 2 actors.
    It returns a list of movies where the actors played together.
    """

    def __init__(self, args: str):
        """Instantiate the CastingFinderCommand
        Instantiate the Parent Class TmdbCliCommand with the args passed and get a TMDB api session
        """
        self.args = args
        super().__init__(self.args)
        self.actors_list = self.args
        self.actors = self.actors_list.split(",")
        self.actor_ids = self._find_actor_ids(self.actors)

    def _find_actor_ids(self, actors_list):
        """
        This functions aims to retrieve TMDB actor'id passed in parameters during the initialization of the CastingFinderCommand
        return actor id from tmdb in a list.
        """
        actor_ids = []
        search = super().tmdb_search()

        for actor in actors_list:
            print(f"Trying to find actor '{actor}' in TMDB...")
            try:
                # take the first
                actor_id = search.person(query=f"{actor}")["results"][0]["id"]
                actor_name = search.person(query=f"{actor}")["results"][0]["name"]
                print(f"Found id for {actor_name}: {actor_id}")
                actor_ids.append(actor_id)
            except:
                raise Exception(f"Could not find {actor}")
        return actor_ids

    def compute(self):
        """Returns a list of movies names where actors id are present"""

        query = super().tmdb_discover().movie(
            with_cast=f"{','.join(str(id) for id in self.actor_ids)}"
        )

        print(f"Found {query['total_results'] } films, with {self.actors_list}")
        for r in query["results"]:
            print(r["original_title"])
        return query["results"]


def main(actors_list):
    """Main processor"""
    casting_finder_command = CastingFinderCommand(actors_list)
    casting_finder_command.compute()
