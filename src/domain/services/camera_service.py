import cv2
import os

RTSP_URL = os.getenv(
    "CAMERA_RTSP",
    "rtsp://admin:CameraNVR2025@192.168.1.103:554/onvif1"
)

_camera = None


def iniciar_camera():
    global _camera

    if _camera is None:
        cam = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
        cam.set(cv2.CAP_PROP_BUFFERSIZE, 2)

        if not cam.isOpened():
            raise RuntimeError("Erro ao abrir câmera RTSP")

        _camera = cam

    return _camera


def gerar_frames():
    cam = iniciar_camera()

    while True:
        success, frame = cam.read()

        if not success:
            continue  # evita flood de print

        _, buffer = cv2.imencode('.jpg', frame)

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            buffer.tobytes() +
            b'\r\n'
        )


def processar_dado(valor):
    return {
        "status": "ok",
        "valor": valor
    }