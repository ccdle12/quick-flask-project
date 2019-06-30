from flask import Flask, jsonify
import json
from simple_app import app
import base64

USER_NAME = 'some-user-1'
USER_PASSWORD = 'some-password'

def test_create_user_route():
    client = app.test_client()
    url = '/user'
    body = json.dumps(dict(name=USER_NAME, password=USER_PASSWORD))
    response = client.post(
            url,
            data=json.dumps(dict(name='some-user-1', password='some-password')),
            content_type='application/json'
    )
    assert response.status_code == 200

def test_login_route():
    client = app.test_client()
    url = '/login'
    credentials = base64.b64encode(b'some-user-1:some-password').decode('utf-8')
    response = client.get(
            url,
            headers={'Authorization': 'Basic ' + credentials}
    )
    TOKEN = json.loads(response.data)['token']
    assert response.status_code == 200

    # Call get users with the token.
    url = '/user'
    response = client.get(
            url,
            headers={'x-access-token': '{}'.format(TOKEN)}
    )
    assert response.status_code == 200
