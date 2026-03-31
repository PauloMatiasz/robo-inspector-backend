import pytest
from flask import Flask, jsonify
from unittest.mock import patch
from src.controllers.robo_controller import RoboController

@pytest.fixture
def client():
    app = Flask(__name__)
    robo_controller = RoboController()

    @app.route("/mover", methods=["POST"])
    def mover_robo_route():
        return robo_controller.mover()

    with app.test_client() as client:
        yield client


# ✅ sucesso
@patch.object(RoboController, "mover")
def test_mover_robo_sucesso(mock_mover, client):
    mock_mover.return_value = ({
        "status": "success",
        "data": {"codigo": 123}
    }), 200

    payload = {"direcao": "frente"}
    res = client.post("/mover", json=payload)

    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "success"
    assert "codigo" in data["data"]


# ✅ validação (não precisa mock)
def test_mover_robo_falta_campo(client):
    res = client.post("/mover", json={})
    assert res.status_code == 400
    data = res.get_json()
    assert data["status"] == "error"
    assert "Campo 'direcao'" in data["message"]


# ✅ erro backend
@patch.object(RoboController, "mover")
def test_mover_robo_erro_backend(mock_mover, client):
    mock_mover.return_value = ({
        "status": "error",
        "message": "Falha ao mover robô"
    }), 500

    payload = {"direcao": "tras"}
    res = client.post("/mover", json=payload)

    assert res.status_code == 500
    data = res.get_json()
    assert data["status"] == "error"
    assert "Falha ao mover robô" in data["message"]