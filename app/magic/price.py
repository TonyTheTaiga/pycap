import click
from app.api import Market


@click.command()
@click.option('--curr', default="BTC", help='Enter A Currency Code, Default is BTC')
@click.option('--ver', default="p", help='enter a version')
@click.argument('ticker', nargs=-1)
def price(curr, ver, ticker):
    market = Market(ver)
    ret, percent_change = market.getPrice(curr.upper(), ticker)
    print(percent_change)
    print(ret)
    for x,y in ret,percent_change:
        if percent_change[y] < 0:
            click.secho(f'{x} : {ret[x]}', fg='red')
    # click.echo(ret)
