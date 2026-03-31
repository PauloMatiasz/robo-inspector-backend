from flask import request
import time


def register_middlewares(app):

    @app.before_request
    def log_request():
        request.start_time = time.time()
        print(f"[REQ] {request.method} {request.path}")

    @app.after_request
    def log_response(response):
        duration = time.time() - request.start_time
        print(f"[RES] {response.status_code} - {duration:.3f}s")
        return response

    @app.errorhandler(Exception)
    def handle_error(e):
        print(f"[ERROR] {str(e)}")
        return {"erro": "Erro interno no servidor"}, 500