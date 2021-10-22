import sys

from tmdbcli.core.command.castingfinder import helloworld
from tmdbcli.core.command.help import helpcommand
def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
    helloworld()
    # build cli
    print("This is the main routine for the entrypoint")

if __name__ == "__main__":
    sys.exit(main())