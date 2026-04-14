from src.domain.services.robo_service import mover
from src.utils.ApiResponse import ApiResponse
from http import HTTPStatus


class RoboController:

    def mover(self, direcao):
        try:
            resultado = mover(direcao)

            return {
                "message": f"Mock movimento {direcao}",
                "data": {"codigo": 200}
            }, 200

        except Exception as e:
            return {
                "message": str(e),
                "data": None
            }, 500