import logging
from logging.handlers import RotatingFileHandler
import os

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .errors import errors

from app.routes.account_routes import account_bp
from app.routes.transaction_routes import transaction_bp
from app.routes.auth_routes import auth_bp


def create_app(config_class='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)
    jwt = JWTManager(app)

    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["200 per day", "50 per hour"]
    )

    app.register_blueprint(account_bp, url_prefix='/account')
    app.register_blueprint(transaction_bp, url_prefix='/transaction')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(errors)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/transactions.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Banking system startup')

    return app
