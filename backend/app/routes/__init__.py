"""routes initialisation"""
from flask import Blueprint
from .address_routes import address_bp
from .cart_details_routes import cart_details_bp
from .cart_routes import cart_bp
from .delivery_info_routes import delivery_info_bp
from .menu_item_routes import menu_item_bp
from .order_details_routes import order_details_bp
from .order_routes import order_bp
from .resturant_routes import resturant_bp
from .rider_routes import rider_bp
from .user_routes import user_bp


def register_routes(app):
    """function to register routes"""
    app.register_blueprint(address_bp, url_prefix='/address')
    app.register_blueprint(cart_details_bp, url_prefix='/cart_details')
    app.register_blueprint(cart_bp, url_prefix='/cart')
    app.register_blueprint(delivery_info_bp, url_prefix='/delivery_info')
    app.register_blueprint(menu_item_bp, url_prefix='/menu_item')
    app.register_blueprint(order_details_bp, url_prefix='/order_details')
    app.register_blueprint(order_bp, url_prefix='/order')
    app.register_blueprint(resturant_bp, url_prefix='/resturant')
    app.register_blueprint(rider_bp, url_prefix='/rider')
    app.register_blueprint(user_bp, url_prefix='/user')

