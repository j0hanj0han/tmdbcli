import click
from tmdbcli.core.command import castingfinder

@click.group()
def main():
    pass

@main.command()
@click.option("--a", prompt=" Enter the first number", type=int)
@click.option("--b", prompt=" Enter the second number", type=int)
def add(a, b):
    value = a + b
    click.echo(" The added value {}".format(value))


@main.command()
@click.option(
    "--withcast", prompt="Enter list of actors, separated by commas", type=str
)
def withcast(withcast):
    """Find common films of actors put in parameters"""
    click.echo(f"List of actors: {withcast}")
    castingfinder.main(withcast)


if __name__ == "__main__":
    main()