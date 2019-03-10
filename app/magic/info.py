import click
from app.api import Market


@click.command()
@click.argument('ticker',nargs=-1)
def info(ticker):
    market = Market() # oh nice, wasn't working beforehand
    data = market.getInfo(ticker)
    click.echo(data)