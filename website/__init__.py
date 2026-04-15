from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from website.routes.auth import auth_bp
    from website.routes.admin import admin_bp
    from website.routes.clerk import clerk_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(clerk_bp)

    return app