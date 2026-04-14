import requests
import os

ESP32_IP = os.getenv("ESP32_IP", "192.168.4.1")


def mover(direcao):
    try:
        if os.getenv("MOCK") == "true":
            return 200

        url = f"http://{ESP32_IP}/command"
        params = {"cmd": direcao}

        response = requests.get(url, params=params, timeout=2)

        return response.status_code

    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha ao comunicar com ESP32: {e}")
        return None