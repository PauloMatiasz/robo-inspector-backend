import cv2
import os

RTSP_URL = os.getenv("CAMERA_RTSP", "rtsp://admin:CameraNVR2025@192.168.1.103:554/onvif1")

# Inicializa a câmera só se necessário
camera = None

def iniciar_camera():
    global camera
    if camera is None:
        camera = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
        camera.set(cv2.CAP_PROP_BUFFERSIZE, 2)
    return camera

def gerar_frames():
    cam = iniciar_camera()
    while True:
        success, frame = cam.read()
        if not success:
            continue
        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

def processar_dado(valor):
    # Simula processamento de dados sem depender da câmera
    return {
        "status": "ok",
        "valor": valor
    }