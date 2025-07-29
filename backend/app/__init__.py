"""app initialization"""

import os
from flask import Flask
from dotenv import load_dotenv

from app.routes.url import register_routes

from .config import Config
from .extensions import db,cors,migrate,jwt
from .models import *
from .admin import init_admin
from .routes.url import user_bp

load_dotenv()

def create_app():
    """create and configure the app"""
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    cors.init_app(app,supports_credentials=True)
    init_admin(app)

    register_routes(app)

    jwt.init_app(app)

    return app
