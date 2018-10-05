import requests
import json
from config import Config
from app.helper import loadJSON, pretty, float_to_str


class Market:

    def __init__(self):
        self.cache = loadJSON()
        self.apiKey = {"X-CMC_PRO_API_KEY": Config.API}

    _base = "https://sandbox-api.coinmarketcap.com"

    _info = _base + "/v1/cryptocurrency/info"

    _latest = _base + "/v1/cryptocurrency/listings/latest"

    _quote = _base + "/v1/cryptocurrency/quotes/latest"

    # _payload = {"id" : "1", "convert" : "USD"}

    def getUSD(self, curr, ticker):
        uid = []
        ret = []

        for x in ticker:
            if self.cache.__contains__(x):
                uid.append(str(self.cache[x]))
            else:
                ret.append({x: "Not Found, Need Valid Ticker"})

        uid = ','.join(uid)
        payload = {"id": uid, "convert": curr}
        request = requests.get(
            self._quote, params=payload, headers=self.apiKey)

        if request.status_code == 200:
            data = request.json()['data']
            for content in data.values():
                ret.append({content['name']: float_to_str(
                    content['quote'][curr]['price'])})
        else:
            # pass a better explanation of why it failed
            ret.append({"status code {}".format(request.status_code): request.json()
                        ["status"]["error_message"]})

        return ret
