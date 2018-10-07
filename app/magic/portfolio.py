import click

from app.api import Portfolio
from app.helper import loadPort, dumpPort


@click.command()
@click.option('--curr', default="USD", help='Enter A Currency Code, Default is USD')
@click.option('--ver', default="p", help='enter a version')
@click.option('--total', default="n", help='Enter "y" to get total Balance')
def portfolio(curr, ver,  total):
    portfolio = Portfolio()
    if total == "n":
        click.echo(portfolio.getBal(curr, ver))
    else:
        click.echo(portfolio.getTot(curr, ver))


@click.command()
def update():
    load = {}
    symbol = input("What coin would you like to update?\n")
    units = float(input("New Amout?\n"))
    load[symbol.strip()] = units
    wallet = loadPort()
    wallet.update(load)
    dumpPort(wallet)
    click.echo(wallet)
