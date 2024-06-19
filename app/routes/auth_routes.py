from flask import Blueprint, request, jsonify
from app.services.auth_services import register_user_service, login_user_service

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    response, status_code = register_user_service(data)
    return jsonify(response), status_code


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    response, status_code = login_user_service(data)
    return jsonify(response), status_code
