from simple_app import app
from simple_app.models import User
from functools import wraps
from flask import request, jsonify
import jwt

def token_required(f):
  """A decorator function that checks whether a jwt passed is valid
  """
  @wraps(f)
  def decorated(*args, **kwargs):
      """The decorator implementation, checks a request for headers and determines
         whether a access token is valid.

      Args:
        request: a request from the end user, contains the access token in the
        header.
      Returns:
        The decorator function or a 401.
      """
      token = None

      if 'x-access-token' in request.headers:
          token = request.headers['x-access-token']

      if not token:
          return jsonify({'message': 'Token is missing'}), 401

      try:
          data = jwt.decode(token, app.config['SECRET_KEY'])
          current_user = User.query.filter_by(public_id=data['public_id']).first()
      except:
          return jsonify({'message': 'Token is invalid'}), 401

      return f(current_user, *args, **kwargs)

  return decorated
