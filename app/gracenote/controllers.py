from flask import Blueprint
import json
from flask import make_response,request, jsonify, abort

#Import model here

providers = Blueprint('gracenote', __name__, url_prefix='/api/gravenote')


@gracenote.route('/')
def index():
    return make_response(jsonify({'status':'ok', 'page': 'home'}))