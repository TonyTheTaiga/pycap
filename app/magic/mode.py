import click
from app.api import Market


@click.command()
@click.option('--curr', default="BTC", help='Enter A Currency Code, Default is BTC')
@click.argument('ticker', nargs=-1)
def price(curr, ticker):
    market = Market()
    ret = market.getUSD(curr.upper(), ticker)
    click.echo(ret)
