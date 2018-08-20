from flask import jsonify
from app.exception import ValidationError
from . import app

def bad_request(message):
    response = jsonify({'error':'bad request', 'message':message})
    response.status_code = 400
    return response

def unauthorize(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response

def forbideen(message):
    response = jsonify({'error':'forbidden', 'message': message})
    response.status_code = 403

@app.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])