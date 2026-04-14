from flask import Blueprint
from src.controllers.robo_controller import RoboController
from src.controllers.camera_controller import CameraController

bp = Blueprint("route01", __name__)

robo_controller = RoboController()
camera_controller = CameraController()


# ROTAS DO ROBÔ (sem body, direto pro front)

@bp.route("/direita", methods=["POST"])
def direita():
    """
    Move o robô para a direita
    ---
    tags:
      - Robô
    responses:
      200:
        description: Movimento executado com sucesso
    """
    return robo_controller.mover("direita")


@bp.route("/esquerda", methods=["POST"])
def esquerda():
    """
    Move o robô para a esquerda
    ---
    tags:
      - Robô
    responses:
      200:
        description: Movimento executado com sucesso
    """
    return robo_controller.mover("esquerda")


@bp.route("/frente", methods=["POST"])
def frente():
    """
    Move o robô para frente
    ---
    tags:
      - Robô
    responses:
      200:
        description: Movimento executado com sucesso
    """
    return robo_controller.mover("frente")

@bp.route("/tras", methods=["POST"])
def tras():
    """
    Move o robô para trás
    ---
    tags:
      - Robô
    responses:
      200:
        description: Movimento executado com sucesso
    """
    return robo_controller.mover("tras")


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