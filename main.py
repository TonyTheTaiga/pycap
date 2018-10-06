import click
from app.magic.price import price
from app.magic.portfolio import portfolio
import __init__


@click.group()
def cli():
    pass


cli.add_command(price)
cli.add_command(portfolio)
