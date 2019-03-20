import click
from app.api import Market
from app.magic.coin import Coin

@click.command()
@click.option('--curr', default="BTC", help='Enter A Currency Code, Default is BTC')
@click.argument('ticker',nargs=-1)
def info(curr, ticker):
    market = Market() 
    curr=curr.upper()
    data = market.getInfo(curr, ticker)
    for content in data.values():
        c = Coin(curr, content)
        c.echo_info()
        print('--------------------------------------')
