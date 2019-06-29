from simple_app import db

class User(db.Model):
    """Model representing a registered user of the API.
      Params:
        id: Primary Key generated by the db.
        public_id: A uuid public key.
        name: The name of the user as string.
        password: A stored and hashed copy of the users password.
        admin: A boolean indicating whether user has admin privileges.
    """
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    admin = db.Column(db.Boolean)

class CoinID(db.Model):
    """CoindID represents a key/value pair of the coin market cap id and the
       ticker symbol for the coin. This will allow users to query for coin 
       information according to the symbol since this feature is not offered
       on coin market cap.
    """
g   id = db.Column(db.Integer, primary_key=True, unique=True)
    symbol = db.Column(db.String(10))
