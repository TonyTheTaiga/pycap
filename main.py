import click
from app.magic.price import price
from app.magic.portfolio import portfolio, update
from app.magic.btc import btc
import __init__
from app.api import Market


@click.group()
def cli():
    pass


cli.add_command(price)
cli.add_command(portfolio)
cli.add_command(btc)
cli.add_command(update)
