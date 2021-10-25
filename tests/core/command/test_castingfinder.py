""" 
"""
from tmdbcli.core.api_client import ApiClient
from tmdbcli.core.command.castingfinder import CastingFinderCommand


def test_find_movies():
    # given
    actors_list = "gerard depardieu, christian clavier"
    api_client = ApiClient()
    # when
    result = CastingFinderCommand(actors_list, api_client).find_movies()
    # then
    assert result == [
        "Astérix & Obélix contre César",
        "Astérix & Obélix Mission Cléopâtre",
        "Mystère à Saint-Tropez",
        "Les Anges gardiens",
        "Convoi exceptionnel",
        "L'An 01",
        "Dites-lui que je l'aime",
    ]
