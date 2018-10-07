import click

from app.api import Portfolio


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
