from flask import jsonify
from simple_app import app

@app.route('/')
def index() -> str:
    """A simple function that returns hello: world"""
    return jsonify('{hello: world}')
