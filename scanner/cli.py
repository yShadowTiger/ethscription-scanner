"""Console script for scanner."""
import sys
import click
from loguru import logger

logger.add(sink=sys.stdout, level="INFO")


@click.command()
def main(args=None):
    """Console script for scanner."""
    click.echo("Replace this message by putting your code into "
               "scanner.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
