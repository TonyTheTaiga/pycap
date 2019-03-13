from requests.compat import urljoin
from config import Config
from app.helper import loadJSON, loadPort, float_to_str, addPort


class Api(object):

    def __init__(self):
        self.sym_id = loadJSON()
        self.base_url = ''
        self.
