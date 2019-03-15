import requests
import json
from requests.compat import urljoin
from config import Config
from app.helper import loadJSON, loadPort, float_to_str, addPort
from app.magic.coin import Coin

class Market(object):

    def __init__(self):
        self.sym_id = loadJSON()
        self.base_url = Config.PRO
        self.apiKey = {"X-CMC_PRO_API_KEY": Config.API}
       
    def makeRequest(self, curr, ticker):
        '''
        make coins here
        '''
        uid = []
        ret = {}

        for x in ticker:
            if self.sym_id.__contains__(x):
                uid.append(str(self.sym_id[x]))
            else:
                ret[x] = "not a valid ticker"
        uid = ','.join(uid)
        payload = {"id": uid, "convert": curr}
        request = requests.get(
            urljoin(self.base_url, Config.QUOTE), params=payload, headers=self.apiKey)

        if request.status_code == 200:
            return request
        else:
            return request

    def getPrice(self, curr, ticker):
        percent_change=[]
        ret={}
        data = self.getInfo(curr,ticker)
        if data == None:
            print('Could not pull data, exiting')
            return ret, None
        for content in data.values():
            coin = Coin(curr,content)
            percent_change.append(coin.coin_dict['percent_change_1h'])
            ret[content['symbol'].lower()] = float_to_str(content['quote'][curr]['price'])
        return ret, percent_change

    def getInfo(self, curr, ticker):
        request = self.makeRequest(curr, ticker)
        data = []
        if request.status_code == 200:
            data = request.json()['data']
            return data
        else:
            return None

class Portfolio(object):

    def __init__(self):
        self.wallet = loadPort()
        self.apiKey = {"X-CMC_PRO_API_KEY": Config.API}

    def getBal(self, curr, ver):
        market = Market()
        ticker = []
        ret = {}
        if self.wallet != {}:
            for x in self.wallet.keys():
                ticker.append(x)
            prices, percent_change = market.getPrice(curr.upper(), ticker)
            for coin, amount in self.wallet.items():
                ret[coin] = amount * float(prices[coin])
        else:
            ret = 'portfolio is empty'

        return (ret), percent_change

    def getTot(self, curr, ver):
        sumthis, _ = self.getBal(curr, ver)
        # calculate net gain/loss percentage here
        return sum(sumthis.values()) if self.wallet != {} else "PORTFOLIO IS EMPTY"
