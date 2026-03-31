import pytest
from src.domain.services.robo_service import mover
from src.domain.services.camera_service import processar_dado
import requests


def test_mover_robo_falha(monkeypatch):
    import requests

    def fake_get(*args, **kwargs):
        raise requests.exceptions.RequestException("Falha de conexão")

    monkeypatch.setattr("src.domain.services.robo_service.requests.get", fake_get)

    status = mover("tras")
    assert status is None

def test_processar_dado():
    valor = 123
    resultado = processar_dado(valor)

    assert resultado["status"] == "ok"
    assert resultado["valor"] == valor