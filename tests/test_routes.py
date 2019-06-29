from flask import Flask, jsonify
import json
from simple_app import app

def test_base_route():
    client = app.test_client()
    url = '/'

    response = client.get(url)
    print(json.loads(response.data)['data']['1'])
    assert response.status_code == 200
