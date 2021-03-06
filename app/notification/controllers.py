from flask import Blueprint
import json
from flask import make_response,request, jsonify, abort

#Import model here

notification = Blueprint('notification', __name__, url_prefix='/api/notification')

#Define notification endpoints here

@notification.route('/')
def index():
    return make_response(jsonify({'status':'ok', 'page': 'home'}))