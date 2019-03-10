import requests
import json
from requests.compat import urljoin
from config import Config
from app.helper import loadJSON, loadPort, float_to_str, addPort


class Market(object):

    def __init__(self, ver):
        self.sym_id = loadJSON()
        self.base_url = ''
        self.apiKey = {"X-CMC_PRO_API_KEY": Config.API}
        self.setVer(ver)

    # Sets the version of the API using the --ver flag

    def setVer(self, version):
        if version == 'p':
            self.base_url = Config.PRO
        else:
            self.base_url = Config.SANDBOX
    # Gets a list of tickers and outputs the price

    def getPrice(self, curr, ticker):
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

        percent_change = []

        if request.status_code == 200:
            data = request.json()['data']
            for content in data.values():
                percent_change.append(content['quote']['BTC']['percent_change_1h'])
                ret[content['symbol'].lower()] = float_to_str(
                    content['quote'][curr]['price'])
        else:
            ret[request.status_code] = request.json()["status"]["error_message"]
            return ret, 0

        return ret, percent_change

class Portfolio(object):

    def __init__(self):
        self.wallet = loadPort()
        self.apiKey = {"X-CMC_PRO_API_KEY": Config.API}

    def getBal(self, curr, ver):
        market = Market(ver)
        ticker = []
        ret = {}
        if self.wallet != {}:
            for x in self.wallet.keys():
                ticker.append(x)
            prices = market.getPrice(curr.upper(), ticker)
            for x, v in self.wallet.items():
                ret[x] = v * float(prices[x])
        else:
            ret = 'portfolio is empty'

        return (ret)

    def getTot(self, curr, ver):
        return sum(self.getBal(curr, ver).values()) if self.wallet != {} else "PORTFOLIO IS EMPTY"
