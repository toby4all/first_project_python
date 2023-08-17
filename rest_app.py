from flask import Flask, request
import json
from db_connector import add_user, get_user, delete_user, update_user

app = Flask(__name__)

# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'POST':
        # getting the json data payload from request
        request_data = request.json
        user_name = request_data.get('name')
        if user_id > 2:
            add_user(user_id, user_name)
            return {'user id': user_id, 'user name': user_name, 'status': 'saved'}, + 200  # status code
        else:
            return {'status': 'error', 'reason': 'id already exist'}, + 500  # status cod


    elif request.method == 'GET':
        request_data = request.json
        user_name = request_data.get('user_id')
        print(len(user_name))
        if len(user_name) <= 2:
            get_user(user_name)
            return {'status': 'ok', 'user_name': user_name}, 200  # status code
        else:
            return {'status': 'error', 'reason': 'no such id'}, +500  # status code
    elif request.method == 'PUT':
        request_data = request.json
        user_name = request_data.get('user_name')
        if len(user_name) <= 2:
            update_user(user_id, user_name)
            return {'status': 'ok', 'user_name': user_name}, + 200  # status code
        else:
            return {'status': 'error', 'reason': 'no such id'}, + 500  # status code
    elif request.method == 'DELETE':
        request_data = request.json
        user_name = request_data.get('user_id')
        if len(user_name) <= 2:
            delete_user(user_id)
            return {'status': 'ok', 'user_deleted': user_id}, + 200  # status code
        else:
            return {'status': 'error', 'reason': 'no such id'}, + 500  # status code



app.run(host='127.0.0.1', debug=True, port=5000)