from flask import jsonify
from http import HTTPStatus


class ApiResponse:
    @staticmethod
    def success(data=None, message=None, code=HTTPStatus.OK):
        return jsonify({
            "status": "success",
            "data": data,
            "message": message,
            "code": code.value
        }), code.value

    @staticmethod
    def error(message=None, data=None, code=HTTPStatus.INTERNAL_SERVER_ERROR):
        return jsonify({
            "status": "error",
            "data": data,
            "message": message,
            "code": code.value
        }), code.value
        