import click

from tmdbcli.core.api_client import ApiClient
from tmdbcli.core.command.castingfinder import CastingFinderCommand


@click.group()
def main():
    pass


@main.command()
@click.option(
    "--actors",
    type=str,
    help="List of actors: string with quotes and separated by commas",
    required=True,
)
def castingfinder(actors):
    """
    Find common movies with actors put in option.
    Parameters: a list of actors.
    Returns a list of movies
    """
    api_client = ApiClient()
    casting_finder_command = CastingFinderCommand(actors, api_client)
    result = casting_finder_command.find_movies()
    click.echo(result)


if __name__ == "__main__":
    main()
