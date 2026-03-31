from src.domain.services.robo_service import mover
from src.domain.services.camera_service import processar_dado
from unittest.mock import patch
import requests 


@patch("src.domain.services.robo_service.requests.get")
def test_mover_sucesso(mock_get):

    class FakeResponse:
        status_code = 200

    mock_get.return_value = FakeResponse()

    resultado = mover("frente")

    mock_get.assert_called_once_with(
        "http://192.168.4.1/command",
        params={"cmd": "frente"},
        timeout=2
    )

    assert resultado == 200


@patch("src.domain.services.robo_service.requests.get")
def test_mover_erro(mock_get):

    mock_get.side_effect = requests.exceptions.RequestException("Falha de conexão")

    resultado = mover("frente")

    assert resultado is None


def test_processar_dado():

    resultado = processar_dado(123)

    assert resultado == {
        "status": "ok",
        "valor": 123
    }