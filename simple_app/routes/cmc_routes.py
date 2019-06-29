from simple_app import app
from simple_app.services import cmc_service
from simple_app.decorators import token_required
# from simple_app.models import User
# from simple_app.decorators import token_required
from flask import jsonify
# import uuid
# import jwt
# from werkzeug.security import generate_password_hash, check_password_hash
# import datetime

@app.route('/map')
def map():
    coin_market_service = cmc_service.CMCService()
    data = coin_market_service.map()

    return jsonify(data)

@app.route('/')
@token_required
def index(current_user):
    """ A simple function that returns hello: world """
    coin_market_service = cmc_service.CMCService()
    data = coin_market_service.get_quote(1)

    return jsonify(data)
