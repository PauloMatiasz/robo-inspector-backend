from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flasgger import Swagger
import os
from src.interface.api import init_routes
from src.interface.middlewares.middleware import register_middlewares

load_dotenv()

app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'API Robo Inspeção',
    'uiversion': 3
}

Swagger(app)

# Configura CORS
CORS(app, origins=os.getenv("CORS_ORIGINS", "*"))

# Registra middlewares
register_middlewares(app)

# Inicializa rotas
init_routes(app)

# Rota raiz
@app.route("/")
def index():
    return {"mensagem": "API Rodando!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)