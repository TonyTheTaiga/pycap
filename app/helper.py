import json
from os import path

# load JSON from file


def loadJSON():
    if path.exists("dict.json"):
        with open('dict.json', 'r') as f:
            return json.load(f)


def loadPort():
    if path.exists('portfolio.json'):
        with open('portfolio.json', 'r') as f:
            return json.load(f)


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
