"""routes initialisation"""
from flask import Blueprint
from app.api.address_view import AddressAPI
from app.api.cart_details_view import CartDetailsAPI
from app.api.cart_view import CartAPI
from app.api.delivery_info_view import DeliveryInfoAPI
from app.api.menu_item_view import MenuItemAPI
from app.api.order_details_view import OrderDetailsAPI
from app.api.order_view import OrderAPI
from app.api.resturant_view import ResturantAPI
from app.api.rider_view import RiderAPI
from app.api.user_view import UserAPI

address_bp = Blueprint('address_bp', __name__, url_prefix='/address')
cartdetail_bp = Blueprint('cartdetails_bp',__name__,url_prefix='/cartdetails')
cart_bp = Blueprint('cart_bp', __name__, url_prefix='/cart')
deliveryinfo_bp = Blueprint('deliveryinfo_bp',__name__,url_prefix='/deliveryinfo')
menuitem_bp = Blueprint('menuitem_bp', __name__, url_prefix='/menuitem')
orderdetail_bp = Blueprint('orderdetails_bp',__name__,url_prefix='/orderdetails')
order_bp = Blueprint('order_bp', __name__, url_prefix='/order')
resturant_bp = Blueprint('resturant_bp',__name__,url_prefix='/resturant')
rider_bp = Blueprint('rider_bp', __name__, url_prefix='/rider')
user_bp = Blueprint('user_bp',__name__,url_prefix='/user')


address_view = AddressAPI.as_view('address_api')
cartdetail_view = CartDetailsAPI.as_view('cartdetails_api')
cart_view = CartAPI.as_view('cart_api')
deiveryinfo_view = DeliveryInfoAPI.as_view('deliveryinfo_api')
menuitem_view = MenuItemAPI.as_view('menuitem_api')
orderdetails_view = OrderDetailsAPI.as_view('orderdetails_api')
order_view = OrderAPI.as_view('order_api')
resturant_view = ResturantAPI.as_view('resturant_api')
rider_view = RiderAPI.as_view('rider_api')
user_view = UserAPI.as_view('user_api')

def register_routes(app):
    """function to register routes"""
    app.register_blueprint(address_bp, url_prefix='/address')
    app.register_blueprint(cartdetail_bp, url_prefix='/cart_details')
    app.register_blueprint(cart_bp, url_prefix='/cart')
    app.register_blueprint(deliveryinfo_bp, url_prefix='/delivery_info')
    app.register_blueprint(menuitem_bp, url_prefix='/menu_item')
    app.register_blueprint(orderdetail_bp, url_prefix='/order_details')
    app.register_blueprint(order_bp, url_prefix='/order')
    app.register_blueprint(resturant_bp, url_prefix='/resturant')
    app.register_blueprint(rider_bp, url_prefix='/rider')
    app.register_blueprint(user_bp, url_prefix='/user')
