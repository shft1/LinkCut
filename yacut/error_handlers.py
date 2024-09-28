from flask import jsonify, render_template

from . import app


class InvalidAPIUsage(Exception):
    status_code = 400

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


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
