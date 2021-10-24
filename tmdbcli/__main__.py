import sys

from tmdbcli.core.cli import main as build_cli


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    build_cli()


if __name__ == "__main__":
    sys.exit(main())
