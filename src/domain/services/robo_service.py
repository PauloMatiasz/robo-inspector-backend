import requests
import os

ESP32_IP = os.getenv("ESP32_IP", "192.168.4.1")


def mover(direcao):
    try:
<<<<<<< HEAD
        response = requests.get(
            f"http://{ESP32_IP}/command?cmd={direcao}",
            timeout=2
        )
        
=======
        url = f"http://{ESP32_IP}/command"
        params = {"cmd": direcao}

        response = requests.get(url, params=params, timeout=2)

>>>>>>> 9e58abe (Robo_inspeção BackEnd Pronto para integrar)
        return response.status_code

    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha ao comunicar com ESP32: {e}")
        return None