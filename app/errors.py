from flask import jsonify
from app.exception import ValidationError
from . import app

"""

Define a error handling functions here

FUNCTIONS:

bad_request(message):   Args=>message; return =>message, error, and status_code(400)
unauthorize(message):   Args=>message; return =>message, error, and status_code(401)
forbidden(message):   Args=>message; return =>message, error, and status_code(403)
validation_error()

"""

def bad_request(message):
    response = jsonify({'error':'bad request', 'message':message})
    response.status_code = 400
    return response

def unauthorize(message):
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response

def forbidden(message):
    response = jsonify({'error':'forbidden', 'message': message})
    response.status_code = 403

@app.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])