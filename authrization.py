from flask_httpauth import HTTPBasicAuth
from flask import Flask, jsonify,abort,make_response
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'sunil':
        return 'sunil'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)