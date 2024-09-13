from flask import Flask
from config.config import Config

def create_app(config_class=Config):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config_class)

    from app.routes import recommendations
    app.register_blueprint(recommendations.bp)

    return app
