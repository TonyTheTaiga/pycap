import os

class Config(object):
    API = os.environ.get('API_KEY') or 'you-key-here'
    SANDBOX = 'https://sandbox-api.coinmarketcap.com'
    PRO = 'https://pro-api.coinmarketcap.com'
    QUOTE = '/v1/cryptocurrency/quotes/latest'
    INFO = '/v1/cryptocurrency/info'
    LATEST = '/v1/cryptocurrency/listings/latest'
    MAP = '/v1/cryptocurrency/map'
    ROOT = os.path.dirname(os.path.abspath(__file__))
