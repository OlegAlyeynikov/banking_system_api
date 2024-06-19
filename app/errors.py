from flask import Blueprint, jsonify

errors = Blueprint('errors', __name__)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@errors.app_errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@errors.app_errorhandler(404)
def not_found(error):
    response = jsonify({'message': 'Not Found'})
    response.status_code = 404
    return response


@errors.app_errorhandler(500)
def internal_server_error(error):
    response = jsonify({'message': 'Internal Server Error'})
    response.status_code = 500
    return response
