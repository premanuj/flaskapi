from flask import Blueprint
import json
from flask import make_response,request, jsonify, abort

#Import model here

providers = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth.route('/')
def index():
    return make_response(jsonify({'status':'ok', 'page': 'home'}))