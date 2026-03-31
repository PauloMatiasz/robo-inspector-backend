from flask import Blueprint
from flasgger import swag_from
from src.controllers.robo_controller import RoboController
from src.controllers.camera_controller import CameraController
from src.docs.swagger.docs import mover_doc

bp = Blueprint("route01", __name__)

robo_controller = RoboController()
camera_controller = CameraController()


@bp.route("/mover", methods=["POST"])
@swag_from(mover_doc)
def mover_robo():
    return robo_controller.mover()


@bp.route("/video", methods=["GET"])
def video():
    """
    Retorna a URL do stream de vídeo
    ---
    tags:
      - Câmera
    responses:
      200:
        description: URL do stream obtida com sucesso
    """
    return camera_controller.video()


@bp.route("/processar", methods=["POST"])
def processar():
    """
    Recebe e processa um valor
    ---
    tags:
      - Processamento
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - valor
          properties:
            valor:
              type: number
              example: 10
    responses:
      200:
        description: Dados processados com sucesso
      400:
        description: Erro de validação
    """
    return camera_controller.receber_dados()