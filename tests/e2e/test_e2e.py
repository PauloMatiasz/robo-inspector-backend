import pytest
from src.app import app as flask_app
from unittest.mock import patch
from flask import jsonify

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert "mensagem" in data
    assert data["mensagem"] == "API Rodando!"


@patch("src.controllers.robo_controller.RoboController.mover")
def test_mover_robo(mock_mover, client):
    mock_mover.return_value = (
    {"status": "success", "data": {"codigo": 999}},
    200
)

    payload = {"direcao": "frente"}
    response = client.post("/mover", json=payload)

    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "codigo" in data["data"]
