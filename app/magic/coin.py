import click
#Class to contain current information on the coins

class Coin(object):

    def __init__(self, curr, data):
        #solution 2: store each data point within a single dictionary
        '''
        self.coin_dict = {}
        for content in data:
            if content != 'quote':
                self.coin_dict[content] = data[content]
            else:
                for quote_data in data['quote'][curr]:
                    self.coin_dict[quote_data] = data['quote'][curr][quote_data]
        '''
        self.fillInfo(curr, data)

    def fillInfo(self, curr, data):
        #data consisting of a single dictionary entry of a coin
        self.last_updated = data['quote'][curr]['last_updated']
        self.symbol = data['symbol']
        #self.circulating_supply = data['circulating_supply']
        #self.total_supply = data['total_supply']
        #self.max_supply = data['max_supply']
        #self.date_added = data['date_added']
        #self.num_market_pairs = data['num_market_pairs']
        #self.tags = data['tags']
        #self.platform = data['platform']
        self.cmc_rank = data['cmc_rank']
        self.volume_24h = data['quote'][curr]['volume_24h']
        self.market_cap = data['quote'][curr]['market_cap']
        self.name = data['name'] 
        self.percent_change_7d = data['quote'][curr]['percent_change_7d']
        self.percent_change_24h = data['quote'][curr]['percent_change_24h']
        self.percent_change_1h = data['quote'][curr]['percent_change_1h']
        self.price = data['quote'][curr]['price']

    def echo_info(self):
        click.secho(f'Last Updated: {self.last_updated}')
        click.secho(f'Symbol: {self.symbol}')
        click.secho(f'CMC Rank: {self.cmc_rank}')
        click.secho(f'Volume 24H: {self.volume_24h}')
        click.secho(f'Market Cap: {self.market_cap}')
        click.secho(f'Name: {self.name}')
        if self.percent_change_7d < 0:
            color = 'red'
        else:
            color = 'green'
        click.secho(f'Percent Change 7D: {self.percent_change_7d}',fg=color)
        if self.percent_change_24h < 0:
            color = 'red'
        else:
            color = 'green'
        click.secho(f'Percent Change 24H: {self.percent_change_24h}',fg=color)
        if self.percent_change_1h < 0:
            color = 'red'
        else:
            color = 'green'
        click.secho(f'Percent Change 1H: {self.percent_change_1h}',fg=color)
        click.secho(f'Price: {self.price}',fg=color)
