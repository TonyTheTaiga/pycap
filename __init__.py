import requests
import json
from config import Config
import os
from os import path
import sys

# If a json file already exists Skip
# else make one

if path.exists(path.join(Config.ROOT, 'dict.json')) is False:
    url = requests.compat.urljoin(Config.PRO, Config.MAP)
    payload = {"listing_status": "active", "start": "1"}
    hd = {"X-CMC_PRO_API_KEY": Config.API}
    request = requests.get(url, params=payload, headers=hd)
    if request.status_code == 200:
        print('here')
        data = request.json()["data"]
        cache = {}
        for content in data:
            cache[content["symbol"].lower()] = content["id"]
        with open(path.join(Config.ROOT, 'dict.json'), 'w') as f:
            json.dump(cache, f)
            f.close()
    else:
        print({"status code {}".format(request.status_code): request.json()
               ["status"]["error_message"]})
        sys.exit(1)
