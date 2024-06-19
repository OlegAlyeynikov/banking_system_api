from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.routes import transaction_bp
from app.services.transaction_services import transfer_service

limiter = Limiter(
    get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)


@transaction_bp.route('/transfer', methods=['POST'])
@jwt_required()
@limiter.limit("10 per minute")
def transfer():
    data = request.get_json()
    response, status_code = transfer_service(data)
    return jsonify(response), status_code
