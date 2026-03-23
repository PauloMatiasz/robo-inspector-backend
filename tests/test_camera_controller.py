import pytest
from flask import Flask
from unittest.mock import patch
from controllers.camera_controller import camera_bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(camera_bp)
    with app.test_client() as client:
        yield client


@patch("controllers.camera_controller.gerar_frames")
def test_video(mock_gerar_frames, client):
    mock_gerar_frames.return_value = iter([b'frame1', b'frame2'])
    res = client.get("/video")
    assert res.status_code == 200
    assert res.mimetype == "multipart/x-mixed-replace"

@patch("controllers.camera_controller.processar_dado")
def test_receber(mock_processar_dado, client):
    mock_processar_dado.return_value = {"status": "ok", "valor": 123}
    res = client.post("/api/dados", json={"valor": 123})
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok", "valor": 123}