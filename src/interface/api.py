from src.interface.routes.route01 import bp as route01_bp

def init_routes(app):
    """
    Registra todos os blueprints da aplicação.
    Adicione novos blueprints aqui conforme necessário.
    """
    app.register_blueprint(route01_bp)