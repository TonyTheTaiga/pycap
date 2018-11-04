import click
from app.api import Market


@click.command()
@click.option('--curr', default="BTC", help='Enter A Currency Code, Default is BTC')
@click.option('--ver', default="p", help='enter a version')
@click.argument('ticker', nargs=-1)
def price(curr, ver, ticker):
    market = Market(ver)
    ret = market.getPrice(curr.upper(), ticker)
    click.echo(ret)
