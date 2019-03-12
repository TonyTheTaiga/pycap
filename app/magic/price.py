import click
from app.api import Market


@click.command()
@click.option('--curr', default="BTC", help='Enter A Currency Code, Default is BTC')
@click.option('--ver', default="p", help='enter a version')
@click.argument('ticker', nargs=-1)
def price(curr, ver, ticker):
    market = Market()
    price_book, percent_change = market.getPrice(curr.upper(), ticker)
    for i,co in enumerate(price_book):        
        if percent_change[i] < 0:
            click.secho(f'{co} : {price_book[co]}', fg='red')
        else:
            click.secho(f'{co} : {price_book[co]}', fg='green')
        
