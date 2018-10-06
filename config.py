import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    API = os.environ.get('API_KEY') or 'your-api-key'
