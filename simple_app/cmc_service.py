from simple_app import app
from requests import Request, Session
import json

class CMCService():
    """
    Constant Private variables used when providing different requests.
    """
    _BASE_URL = 'https://pro-api.coinmarketcap.com/v1'
    _QUOTES = '/cryptocurrency/quotes/latest'
    _MAP = '/cryptocurrency/map'

    """
    Default headers for sending requests to coin market cap.
    """
    _headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': app.config['CMC_SECRET_KEY']
    }

    """ Session for each request. """
    _session = None

    def __init__(self):
      self._session = Session()
      self._session.headers.update(self._headers)
      
    def get_quote(self, coin_id):
       """ Get a quote for a given id """
       url = '{}{}'.format(self._BASE_URL, self._QUOTES)
       parameters = {
         'id': coin_id
       }

       response = self._session.get(url, params=parameters)

       return json.loads(response.text)

    def map(self):
      url = '{}{}'.format(self._BASE_URL, self._MAP)
      response = self._session.get(url)

      return json.loads(response.text)


