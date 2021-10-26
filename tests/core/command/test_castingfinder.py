"""
This test aims to check the whole working flow of the application. It makes a real call to the API and retrieve real data.
It's a beta version.
In a near future we need to add unit test with mocking component for each function when it's necessary (like api call) in a order to test properly.
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
