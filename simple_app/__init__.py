from flask import Flask
from flask_sqlalchemy import SQLAlchemy

""" Loads the secret variables from the instance folder """
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

""" Connects to an instance of SQLALCHEMY """
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
db.create_all()

from simple_app import models
from simple_app import decorators
from simple_app.routes import user_routes, cmc_routes
from simple_app.services import cmc_service
