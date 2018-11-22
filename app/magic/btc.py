import click
from app.api import Market


@click.command()
@click.option('--curr', default="USD", help='Enter A Currency Code, Default is BTC')
@click.option('--ver', default="p", help='enter a version')
def btc(curr, ver):
    market = Market(ver)
    ret = market.getPrice(curr.upper(), ['btc', ])
    click.echo(ret)
