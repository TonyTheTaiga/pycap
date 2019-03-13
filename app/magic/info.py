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
    #ids = (list(data.values())[0]).keys()
    for content in data.values():
        c = Coin(curr, content)
        for key in c.coin_dict:
            if type(c.coin_dict[key]) == int or type(c.coin_dict[key]) == float:
                if c.coin_dict[key] < 0:
                    click.secho(f'{key}: {c.coin_dict[key]}', fg='red')
                else:
                    click.secho(f'{key}: {c.coin_dict[key]}', fg='green')
            else:
                click.secho(f'{key}: {c.coin_dict[key]}')

        '''
        for i in ids:
            if i != 'quote':
                print(str(i)+": "+str(content[i])) 
            else:
                for quote_data in content['quote'][curr]:
                    print(str(quote_data)+": "+str(content['quote'][curr][quote_data]))
        '''
        print('--------------------------------------')