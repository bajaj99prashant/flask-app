from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

# creating uninitialized extention instance
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # configuration handling
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # extentions handling
    db.init_app(app)

    # registering blueprints after importing them
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app