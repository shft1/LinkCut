from http import HTTPStatus

from flask import jsonify, render_template

from . import app


class InvalidAPIUsage(Exception):
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message, status=None):
        super().__init__()
        self.message = message
        if status is not None:
            self.status_code = status

    def to_dict(self):
        return dict(message=self.message)


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(HTTPStatus.NOT_FOUND)
def not_found(error):
    return render_template('404.html'), HTTPStatus.NOT_FOUND
