from flask import jsonify
from simple_app import app
from simple_app import cmc_service

@app.route('/map')
def map():
  coin_market_service = cmc_service.CMCService()
  data = coin_market_service.map()

  return jsonify(data)

@app.route('/')
def index():
    """ A simple function that returns hello: world """
    coin_market_service = cmc_service.CMCService()
    data = coin_market_service.get_quote(1)

    return jsonify(data)
