from simple_app import app, db
from simple_app.services import cmc_service
from simple_app.decorators import token_required
from simple_app.models import CoinID
from flask import jsonify, request

@app.before_first_request
def fetch_coin_ids():
    """Function that runs before the first request. It fetches all the ids 
       from the coin market cap API and writes it to the db along with the
       corresponding symbol.
    """
    print('Caching the coin ids...')
    coin_market_service = cmc_service.CMCService()
    data = coin_market_service.map()

    coins = []
    for d in data['data']:
        exists = bool(CoinID.query.filter_by(id=int(d['id'])).first())
        if not exists:
            coins.append(CoinID(id=int(d['id']), symbol=d['symbol']))

    db.session.add_all(coins)
    db.session.commit()

@app.route('/quote', methods=['GET'])
@token_required
def get_quote(current_user):
    """Request to retrieve a quote given a symbol. The symbol is passed as a
        query string in the url e.g. '/quote?symbol=btc'.
    """
    symbol = request.args['symbol']
    coin = CoinID.query.filter_by(symbol=symbol.upper()).first()
    if not coin:
        return jsonify({'message': 'coin does not exist'}), 404

    coin_market_service = cmc_service.CMCService()
    data = coin_market_service.get_quote(coin.id)

    return jsonify(data)
