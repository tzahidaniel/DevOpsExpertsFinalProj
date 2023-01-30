from flask import Flask, request
from db_connector import get_user, add_user, update_user, delete_user, check_user_existence
from flask import jsonify

app = Flask(__name__)
schema_name = "freedb_devops"


@app.route('/users/<user_id>', methods=['GET'])
def app_get_user(user_id):
    print('GET_USER_METHOD')
    user = get_user(user_id)
    if user:
        return jsonify({'status': 'ok', 'user_name': user}, 200)  # error code return value.
    return jsonify({'status': 'error', 'message': 'no such id'}, 500)  # error code return value.


@app.route('/users', methods=['POST'])
def app_add_user():
    print('ADD_USER_METHOD')
    request_data = request.json
    user_name = request_data.get('user_name')
    user, user_id = add_user(user_name)
    return (jsonify({'user': user, 'id': user_id, 'status': 'saved'}, 200))  # status code


@app.route('/users/<user_id>', methods=['DELETE'])
def app_delete_user_by_id(user_id):
    print('DELETE_USER_METHOD')
    if not check_user_existence(user_id=user_id):
        return jsonify({'status': 'error', 'message': 'no such id'}, 500)  # error code return value.
    if delete_user(user_id=user_id):
        return jsonify({'status': 'ok', 'message': 'user_deleted: ' + user_id}, 200)  # error code return value.


@app.route('/users/<user_id>', methods=['PUT'])
def app_update_user(user_id):
    print('UPDATE_USER_METHOD')
    if check_user_existence(user_id):
        request_data = request.json
        user_name = request_data.get('user_name')
        update_user(user_id, user_name)
        return jsonify({'status': 'success', 'message': f'user {user_name[1]} updated'}, 200)
    else:
        return jsonify({'status': 'error', 'message': 'no such id'}, 500)  # error code return value.


app.run(host='127.0.0.1', debug=True, port=5000)

"""
On success: return JSON : {“status”: “ok”, “user_name”: <USER_NAME>} + code: 200
On error: return JSON : {“status”: “error”, “message”: ”no such id”} + code: 500
"""
