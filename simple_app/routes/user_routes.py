from simple_app import app, db
from simple_app.models import User
from simple_app.decorators import token_required
from flask import jsonify, request, make_response
import uuid
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

# User end points
def build_user_dict(user):
    """Builds a user dict given a user model.

    Args:
        user: a user model read from the db.
    Returns:
        A dict, user information in key,value format.
    """
    user_dict = {}
    user_dict['public_id'] = user.public_id
    user_dict['name'] = user.name
    user_dict['password'] = user.password
    user_dict['admin'] = user.admin
    
    return user_dict

@app.route('/user', methods=['POST'])
def create_user():
    """Creates a user in the database.

    Args:
      name: The username of the user as a string.
      password: The password for the user as a string, this will be hashed
                when written to the db.
    Returns:
      A message in json format, indicating the user was succesfully written.
    """
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(
        public_id=str(uuid.uuid4()),
        name=data['name'],
        password=hashed_password,
        admin=False)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created'})

@app.route('/user', methods=['GET'])
@token_required
def get_all_user(current_user):
    """Gets all registered users from the db.

    Args:
      None
    Returns:
      A list of user dicts as json.
    """
    users = User.query.all()

    return jsonify([build_user_dict(user) for user in users])

@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_one_user(current_user, public_id):
    """Gets a single user from the db.

    Args:
      public_id: The public id of the a user.
    Returns:
      A user dict as json.
    """
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message': 'User not found'})

    return jsonify({'user': build_user_dict(user)})

@app.route('/login')
def login():
    """Login for a registered user.

    Args:
      authorization: basic auth - username and password.
    Returns:
      jwt with a time delta of 30 minutes.
    """
    auth = request.authorization

    error_message = jsonify({'message': 'Could not verify'})
    error_response = make_response(
        error_message,
        401,
        {'WWW-Authenticate' : 'Basic realm="Login Required"'}
    )

    if not auth or not auth.username or not auth.password:
        return error_response

    user = User.query.filter_by(name=auth.username).first()
    if not user:
        return error_response

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }, app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')})

    return error_response
