from src.domain.services.camera_service import processar_dado

def test_processar_dado():
    resultado = processar_dado(10)

    assert resultado["status"] == "ok"
    assert resultado["valor"] == 10