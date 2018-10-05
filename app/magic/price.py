import click
from app.market import Market


@click.command()
@click.option('--curr', default="BTC", help='Enter A Currency Code, Default is BTC')
@click.argument('ticker', nargs=-1)
def cli(curr, ticker):
    a = Market()
    ret = a.getUSD(curr.upper(), ticker)
    click.echo(ret)
