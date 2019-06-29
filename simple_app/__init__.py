from flask import Flask
import os

""" Loads the secret variables from the instance folder """
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

from simple_app import end_points
