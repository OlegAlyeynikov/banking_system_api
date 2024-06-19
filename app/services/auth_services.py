from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from app.models import users, next_user_id, User


def register_user_service(data):
    global next_user_id

    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        return {'error': 'Invalid input'}, 400

    for user in users.values():
        if user.username == username:
            return {'error': 'Username already exists'}, 400

    user_id = next_user_id
    hashed_password = generate_password_hash(password)
    users[user_id] = User(user_id, username, hashed_password)
    next_user_id += 1

    return {'user_id': user_id, 'username': username}, 201


def login_user_service(data):
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        return {'error': 'Invalid input'}, 400

    for user in users.values():
        if user.username == username and check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.user_id)
            return {'access_token': access_token}, 200

    return {'error': 'Invalid credentials'}, 401
