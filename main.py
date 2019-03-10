import click
from app.magic.price import price
from app.magic.portfolio import portfolio, update
from app.magic.btc import btc
from app.api import Market
from app.magic.info import info

@click.group()
def cli():
    pass

cli.add_command(price)
cli.add_command(portfolio)
cli.add_command(btc)
cli.add_command(update)
cli.add_command(info)

# For Testing Purposes
if __name__ == '__main__':
    cli()
