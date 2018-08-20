from flask import Blueprint
import json
from flask import make_response,request, jsonify, abort

#Import model here

gracenote = Blueprint('gracenote', __name__, url_prefix='/api/gracenote')


#Define gracenote api endpoints here

@gracenote.route('/')
def index():
    return make_response(jsonify({'status':'ok', 'page': 'home'}))