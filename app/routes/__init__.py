from flask import Blueprint

account_bp = Blueprint('account', __name__)
transaction_bp = Blueprint('transaction', __name__)
auth_bp = Blueprint('auth', __name__)

from . import account_routes, transaction_routes, auth_routes
