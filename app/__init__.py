import requests
import json
from config import Config
from os import path

# If a json file already exists Skip
# else make one

if path.exists("dict.json") is False:
    url = "https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/map"
    payload = {"listing_status": "active", "start": "1"}
    hd = {"X-CMC_PRO_API_KEY": Config.API}
    request = requests.get(url, params=payload, headers=hd)
    data = request.json()["data"]
    if request.status_code == 200:
        cache = dict()
        for content in data:
            cache[content["symbol"].lower()] = content["id"]
        with open('dict.json', 'w') as f:
            json.dump(cache, f)
            f.close()
    else:
        print("Did not work, please check the error\n{}".format(request.text))
