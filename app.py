from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

#aqui voce inicia as rotas com o init routes la do seu api.py

load_dotenv()

app = Flask(__name__)

# CORS pegando do .evn
CORS(app, origins=os.getenv("CORS_ORIGINS", "*"))

# Pela pela variavel do env ou pela port 
port = int(os.getenv("FLASK_PORT", 5000))
debug = os.getenv("DEBUG", "True") == "True"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=debug)