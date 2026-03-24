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
        #interessante voce logar isso, adiconar prints no app para saber onde seu app esta passando e o que esta fazendo, para facilitar o debug, principalmente quando for rodar o backend e o esp32 juntos, para saber se o backend esta conseguindo se comunicar com o esp32 ou se esta dando timeout, etc...
        return None
#Caso o esp32 nao se envie, ele vai continuar rodando o backend
#contina rodando o back mas deve avisar que nao conectou com o esp32, para o usuario saber que tem algo errado, e para facilitar o debug, voce pode usar um logger para isso, ou simplesmente usar prints, o importante e ter uma forma de saber o que esta acontecendo no seu app, principalmente quando for rodar o backend e o esp32 juntos.