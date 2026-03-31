from flask import request
from src.domain.services.robo_service import mover
from src.utils.ApiResponse import ApiResponse
from http import HTTPStatus


class RoboController:

    def mover(self):
        data = request.get_json()

        # Validação
        if not data or "direcao" not in data:
            return ApiResponse.error(
                message="Campo 'direcao' é obrigatório",
                code=HTTPStatus.BAD_REQUEST
            )

        direcao = data["direcao"]

        resultado = mover(direcao)

        if resultado is None:
            return ApiResponse.error(
                message="Falha ao mover robô",
                code=HTTPStatus.INTERNAL_SERVER_ERROR
            )

        return ApiResponse.success(
            data={"codigo": resultado},
            message="Movimento executado com sucesso",
            code=HTTPStatus.OK
        )