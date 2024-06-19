from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from . import account_bp
from ..services.account_services import create_account_service, deposit_service, withdraw_service

limiter = Limiter(
    get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)


@account_bp.route('/create_account', methods=['POST'])
@jwt_required()
@limiter.limit("10 per minute")
def create_account():
    data = request.get_json()
    response, status_code = create_account_service(data)
    return jsonify(response), status_code


@account_bp.route('/deposit', methods=['POST'])
@jwt_required()
@limiter.limit("20 per minute")
def deposit():
    data = request.get_json()
    response, status_code = deposit_service(data)
    return jsonify(response), status_code


@account_bp.route('/withdraw', methods=['POST'])
@jwt_required()
@limiter.limit("20 per minute")
def withdraw():
    data = request.get_json()
    response, status_code = withdraw_service(data)
    return jsonify(response), status_code
