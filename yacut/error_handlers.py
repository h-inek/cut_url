from http import HTTPStatus

from flask import render_template, jsonify

from . import app


class DuplicateValue(Exception):
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message, status_code=None, encoding='utf-8'):
        super().__init__()
        self.encoding = encoding
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


class InvalidUsage(Exception):
    status_code = HTTPStatus.BAD_REQUEST

    def __init__(self, message, status_code=None, encoding='utf-8'):
        super().__init__()
        self.encoding = encoding
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


@app.errorhandler(InvalidUsage)
def invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(DuplicateValue)
def invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error):
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def page_not_found(error):
    return render_template('500.html'), HTTPStatus.INTERNAL_SERVER_ERROR
