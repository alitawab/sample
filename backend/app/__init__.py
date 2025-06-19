"""app initialization"""

import os
from flask import Flask
from dotenv import load_dotenv

from .config import Config
from .extensions import db,cors,migrate
from .models import *
from app.routes import register_routes

load_dotenv()

def create_app():
    """create and configure the app"""
    app = Flask(__name__)
    app.config.from_object(Config)

    app.config['SQLAlCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app,db)
    cors.init_app(app)

    register_routes(app)

    return app
