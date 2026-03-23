import requests
import os

ESP32_IP = os.getenv("ESP32_IP", "192.168.4.1")

def mover(direcao):
    try:
        response = requests.get(
            f"http://{ESP32_IP}/command?cmd={direcao}",
            timeout=2
        )
        return response.status_code
    except:
        return None