from flask import Blueprint
import json
from flask import make_response,request, jsonify, abort
# from app import db
from app.models import Provider

providers = Blueprint('providers', __name__, url_prefix='/providers')


datas = [{'name': 'fdsaf', 'name_id':24},{'name': 'anuj', 'name_id':34},{'name': 'ajlknuj', 'name_id':54}]
data = {'name': 'fdsaf', 'name_id':24}

@providers.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@providers.route('/')
def index():
    return make_response(jsonify(datas))

@providers.route('/name/<int:age>', methods=['GET'])
def data_by_id(age):
    for i in datas:
        if i['name_id'] ==age:
            return make_response(jsonify(i))
    else:
        return make_response('Invalid input')

@providers.errorhandler(400)  
@providers.route('/add/', methods=['POST'])
def add():
    print(request)
    if not request.json :
        abort(400)
    print(request)
    return make_response(jsonify({
        'status': 200
    }))