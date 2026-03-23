Backend - Sistema de Controle WiFi ESP32
🔹 Descrição

Backend em Flask para controle de robô via ESP32 e streaming de vídeo da câmera.
Permite integração com front-end React ou qualquer cliente que consuma a API.

Controle do robô: frente, trás, esquerda, direita, parar, lanterna
Telemetria: posição X/Y, bateria, status da lanterna
Streaming de vídeo via RTSP
Configurações via .env
Testes unitários com pytest

🔹 Estrutura do Projeto
backend/
 ├─ app.py                 
 ├─ controllers/           
 │   ├─ robo_controller.py
 │   └─ camera_controller.py
 ├─ services/              
 │   ├─ robo_service.py
 │   └─ camera_service.py
 ├─ tests/                 
 │   ├─ test_robo.py
 │   └─ test_camera_controller.py
 ├─ requirements.txt       
 └─ .env                   
 
🔹 Variáveis de Ambiente (.env)

ESP32_IP=192.168.4.1
CAMERA_RTSP=rtsp://admin:CameraNVR2025@192.168.1.103:554/onvif1
FLASK_ENV=development
FLASK_PORT=5000
DEBUG=True
CORS_ORIGINS=http://localhost:3000

🔹 Instalação
Criar e ativar virtualenv:
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

Instalar dependências:
pip install -r requirements.txt

🔹 Rodando o Backend

python app.py
O backend roda na porta definida em FLASK_PORT (default: 5000)
CORS configurado para permitir chamadas do React (CORS_ORIGINS)

🔹 Testes Unitários

Rodar todos os testes:

pytest

Rodar um teste específico:

pytest tests/test_camera_controller.py

✅ Todos os testes devem passar antes da integração com o React.
