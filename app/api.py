import requests
import json
from requests.compat import urljoin
from config import Config
from app.helper import loadJSON, loadPort, float_to_str

_base = "https://sandbox-api.coinmarketcap.com"

_info = "/v1/cryptocurrency/info"

_latest = "/v1/cryptocurrency/listings/latest"

_quote = "/v1/cryptocurrency/quotes/latest"


class Market:

    def __init__(self):
        self.sym_id = loadJSON()
        self.apiKey = {"X-CMC_PRO_API_KEY": Config.API}

    def getUSD(self, curr, ticker):
        uid = []
        ret = dict()

        for x in ticker:
            if self.sym_id.__contains__(x):
                uid.append(str(self.sym_id[x]))
            else:
                ret[x] = "non valid ticker"

        uid = ','.join(uid)
        payload = {"id": uid, "convert": curr}
        request = requests.get(
            urljoin(_base, _quote), params=payload, headers=self.apiKey)

        if request.status_code == 200:
            data = request.json()['data']
            for content in data.values():
                ret[content['symbol'].lower()] = float_to_str(
                    content['quote'][curr]['price'])
        else:
            ret[request.status_code] = request.json()["status"]["error_message"]

        return ret


class Portfolio:

    def __init__(self):
        self.wallet = loadPort()
        self.apiKey = {"X-CMC_PRO_API_KEY": Config.API}

    def getBal(self, curr):
        market = Market()
        ticker = []
        ret = dict()

        for x in self.wallet.keys():
            ticker.append(x)
        prices = market.getUSD(curr.upper(), ticker)
        for x, v in self.wallet.items():
            ret[x] = v * float(prices[x])

        return (ret)

    def getTot(self, curr):
        return sum(self.getBal(curr).values())
