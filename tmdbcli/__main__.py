import sys
import os

from tmdbcli.core.cli import main as build_cli
from tmdbcli.utils.errors import ApiKeyNotFound


def main():
    """The main routine of TMDB Cli."""

    if "API_KEY" in os.environ:
        build_cli()
    else:
        raise ApiKeyNotFound()


if __name__ == "__main__":
    sys.exit(main())
