import click
from app.api import Market


@click.command()
@click.option('--curr', default="BTC", help='Enter A Currency Code, Default is BTC')
@click.option('--ver', default="p", help='enter a version')
@click.argument('ticker', nargs=-1)
def price(curr, ver, ticker):
    market = Market(ver)
    ret, percent_change = market.getPrice(curr.upper(), ticker)
    #print(percent_change)
    #print(ret)
    for i,x in enumerate(ret):        
        if percent_change[i] < 0:
            click.secho(f'{x} : {ret[x]}', fg='red')
        else:
            click.secho(f'{x} : {ret[x]}', fg='green')
        
    click.echo(ret)
