from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

# creating uninitialized extention instance
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)

    # configuration handling
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # extentions handling
    db.init_app(app)
    login_manager.init_app(app)

    # registering blueprints after importing them
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app