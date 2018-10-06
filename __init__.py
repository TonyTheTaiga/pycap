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
    if request.status_code == 200:
        data = request.json()["data"]
        cache = dict()
        for content in data:
            cache[content["symbol"].lower()] = content["id"]
        with open('dict.json', 'w') as f:
            json.dump(cache, f)
            f.close()
    else:
        print({"status code {}".format(request.status_code): request.json()
               ["status"]["error_message"]})
