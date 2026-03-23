from services.robo_service import mover
from unittest.mock import patch
from services.camera_service import processar_dado

@patch("services.robo_service.requests.get")
def test_mover_sucesso(mock_get):
    mock_get.return_value.status_code = 200

    resultado = mover("frente")

    mock_get.assert_called_once_with(
        "http://192.168.4.1/command?cmd=frente",
        timeout=2
    )
    assert resultado == 200

@patch("services.robo_service.requests.get")
def test_mover_erro(mock_get):
    mock_get.side_effect = Exception("Erro")

    resultado = mover("frente")

    assert resultado is None
    
def test_processar_dado():
    resultado = processar_dado(123)
    assert resultado == {"status": "ok", "valor": 123}