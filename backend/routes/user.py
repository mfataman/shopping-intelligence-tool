from flask import Blueprint, request, jsonify

user_routes = Blueprint('user_routes', __name__)

# Sample user data
users = []

@user_routes.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username and password:
        users.append({'username': username, 'password': password})
        return jsonify({'message': 'User registered successfully!'}), 201
    return jsonify({'message': 'Username and password required!'}), 400

@user_routes.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    for user in users:
        if user['username'] == username and user['password'] == password:
            return jsonify({'message': 'Login successful!'}), 200
    return jsonify({'message': 'Invalid username or password!'}), 401

@user_routes.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

