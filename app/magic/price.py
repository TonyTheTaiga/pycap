import click
from app.api import Market

@click.command()
@click.option('--curr', default="BTC", help='Enter A Currency Code, Default is BTC')
@click.option('--ver', default="p", help='enter a version')
@click.argument('ticker', nargs=-1)
def price(curr, ver, ticker):
    market = Market()
    price_book, percent_change = market.getPrice(curr.upper(), ticker)
    click.echo(percent_change)       
    for i, coin in enumerate(price_book): 
        click.secho('**************************')
        if percent_change[i] < 0:
            click.secho(f'{coin} : -->{price_book[coin]}<--', fg='red')
   
        else:
            click.secho(f'{coin} IS AT -->{price_book[coin]}<--', fg='green')
    click.secho('**************************')
        
