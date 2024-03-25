import os
from flask import Flask
from .extensions import db, migrate, jwt
# from .routes import configure_routes

def create_app():
    app = Flask(__name__)
    
    # Configurações da aplicação
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', 'postgresql://user:password@db/mydatabase')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv(
        'JWT_SECRET_KEY', 'your_fallback_secret_key')
    
    # Inicializa as extensões com o app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Registra os Blueprints
    from .classification.blueprint import classification_bp
    from .user.blueprint import user_bp
    app.register_blueprint(user_bp)
    app.register_blueprint(classification_bp)

    return app