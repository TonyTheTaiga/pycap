#Class to contain current information on the coins

class Coin(object):

    def __init__(self, curr, data):
        #solution 2: store each data point within a single dictionary
        
        self.coin_dict = {}
        for content in data:
            if content != 'quote':
                self.coin_dict[content] = data[content]
            else:
                for quote_data in data['quote'][curr]:
                    self.coin_dict[quote_data] = data['quote'][curr][quote_data]
        
        #self.fillInfo(curr, data)
    '''
    def fillInfo(self, curr, data):
        if data[0] == 400:
            print("Unable to process request.")
        else: 
            #data consisting of a single dictionary entry of a coin
            self.name = data['name']
            self.symbol = data['symbol']
            self.circulating_supply = data['circulating_supply']
            self.total_supply = data['total_supply']
            self.max_supply = data['max_supply']
            self.date_added = data['date_added']
            self.num_market_pairs = data['num_market_pairs']
            self.tags = data['tags']
            self.platform = data['platform']
            self.cmc_rank = data['cmc_rank']
            #beneath is in quote dict
            self.price = data['quote'][curr]['price']
            self.volume_24h = data['quote'][curr]['volume_24h']
            self.percent_change_1h = data['quote'][curr]['percent_change_1h']
            self.percent_change_24h = data['quote'][curr]['percent_change_24h']
            self.percent_change_7d = data['quote'][curr]['percent_change_7d']
            self.market_cap = data['quote'][curr]['market_cap']
            self.last_updated = data['quote'][curr]['last_updated']
    '''