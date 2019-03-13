import click
from app.api import Market


@click.command()
@click.argument('ticker',nargs=-1)
@click.option('--curr', default="BTC", help='Enter A Currency Code, Default is BTC')
@click.argument('')
def info(curr, ticker):
    market = Market() 
    data = market.getInfo(curr, ticker)
    ids = (list(data.values())[0]).keys()
    for content in data.values():
        for i in ids:
            if i != 'quote':
                print(str(i)+": "+str(content[i]))
            else:
                for quote_data in content['quote']['USD']:
                    print(str(quote_data)+": "+str(content['quote']['USD'][quote_data]))
        print('--------------------------------------')