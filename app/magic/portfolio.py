import click

from app.api import Portfolio


@click.command()
@click.option('--curr', default="USD", help='Enter A Currency Code, Default is USD')
@click.option('--total', default="n", help='Enter "y" to get total Balance')
def portfolio(curr, total):
    portfolio = Portfolio()
    if total == "n":
        click.echo(portfolio.getBal(curr))
    else:
        click.echo(portfolio.getTot(curr))
