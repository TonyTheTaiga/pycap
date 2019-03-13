import requests
import json
from requests.compat import urljoin
from config import Config
from app.helper import loadJSON, loadPort, float_to_str, addPort

class Market(object):

    def __init__(self):
        self.sym_id = loadJSON()
        self.base_url = ''
        self.apiKey = {"X-CMC_PRO_API_KEY": Config.API}
        self.setVer('p')

    # Sets the version of the API using the --ver flag

    def setVer(self, version):
        if version == 'p':
            self.base_url = Config.PRO
        else:
            self.base_url = Config.SANDBOX

    # Gets a list of tickers and outputs the price
    def makeRequest(self, curr, ticker):
        uid = []
        ret = {}
        
        for x in ticker:
            if self.sym_id.__contains__(x):
                uid.append(str(self.sym_id[x]))
            else:
                ret[x] = "not a valid ticker"
        uid = ','.join(uid)
        payload = {"id":uid, "convert":curr}
        request = requests.get(
            urljoin(self.base_url, Config.QUOTE), params=payload, headers=self.apiKey)
        
        return request

    def getPrice(self, curr, ticker):
        #uid = []
        #ret = {}

        #for x in ticker:
        #     if self.sym_id.__contains__(x):
        #         #print(type(str(self.sym_id[x])))
        #         uid.append(str(self.sym_id[x]))
        #     else:
        #         ret[x] = "not a valid ticker"

        # uid = ','.join(uid)
        # payload = {"id": uid, "convert": curr}
        # request = requests.get(
        #     urljoin(self.base_url, Config.QUOTE), params=payload, headers=self.apiKey)

        request = self.makeRequest(curr, ticker)
        
        percent_change = []
        ret = {}

        if request.status_code == 200:
            data = request.json()['data']
            for content in data.values():
                percent_change.append(content['quote'][curr]['percent_change_1h'])
                ret[content['symbol'].lower()] = float_to_str(
                    content['quote'][curr]['price'])
        else:
            ret[request.status_code] = request.json()["status"]["error_message"]
            return ret, 0

        return ret, percent_change

    def getInfo(self, curr, ticker):
        # uid = []
        # ret = {}

        # for x in ticker:
        #     if self.sym_id.__contains__(x):
        #         uid.append(str(self.sym_id[x]))
        #     else:
        #         ret[x] = "not a valid ticker"

        # uid = ','.join(uid)
        # payload = {"id": uid}
        # request = requests.get(
        #     urljoin(self.base_url, Config.QUOTE), params=payload, headers=self.apiKey)

        request = self.makeRequest(curr, ticker)

        data = []
        
        if request.status_code == 200:
            data = request.json()['data']

        return data

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
        sumthis, _ = self.getBal(curr,ver)
        #calculate net gain/loss percentage here
        return sum(sumthis.values()) if self.wallet != {} else "PORTFOLIO IS EMPTY"
