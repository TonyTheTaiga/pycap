import json
import requests
from config import Config
from os import path
import sys
# load JSON from file


def loadJSON():
    if path.exists(path.join(Config.ROOT, 'dict.json')):
        with open(path.join(Config.ROOT, 'dict.json'), 'r') as f:
            return json.load(f)
    else:
        sys.exit(1)


def loadPort():
    if path.exists(path.join(Config.ROOT, 'portfolio.json')):
        with open(path.join(Config.ROOT, 'portfolio.json'), 'r') as f:
            return json.load(f)
    else:
        sys.exit(1)


def addPort():
    None


# pretty prints JSON data
def pretty(data):
    return print(json.dumps(data, indent=4, separators=(',', ': ')))

# takes float and converts it to e-8


def float_to_str(f: int):
    float_string = repr(float(round(f, 8)))
    if 'e' in float_string:  # detect scientific notation
        digits, exp = float_string.split('e')
        digits = digits.replace('.', '').replace('-', '')
        exp = int(exp)
        # minus 1 for decimal point in the sci notation
        zero_padding = '0' * (abs(int(exp)) - 1)
        sign = '-' if f < 0 else ''
        if exp > 0:
            float_string = '{}{}{}.0'.format(sign, digits, zero_padding)
        else:
            float_string = '{}0.{}{}'.format(sign, zero_padding, digits)
    return float_string


def createMap(base):
    if path.exists(path.join(Config.ROOT, 'dict.json')) is False:
        url = requests.compat.urljoin(base, Config.MAP)
        payload = {"listing_status": "active", "start": "1"}
        hd = {"X-CMC_PRO_API_KEY": Config.API}
        request = requests.get(url, params=payload, headers=hd)
        if request.status_code == 200:
            print('here')
            data = request.json()["data"]
            cache = {}
            for content in data:
                cache[content["symbol"].lower()] = content["id"]
            with open('./dict.json', 'w') as f:
                json.dump(cache, f)
                f.close()
        else:
            print({"status code {}".format(request.status_code): request.json()
                   ["status"]["error_message"]})
