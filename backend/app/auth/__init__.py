"""auth route initialization"""
from app.auth.routes import auth_bp

def register_routes(app):
    """function to initialize auth route"""
    app.register_blueprint(auth_bp, url_prefix='/auth')
