"""url routes """
from flask import Blueprint

from app.api.address_view import AddressAPI
from app.api.cart_details_view import CartDetailsAPI
from app.api.cart_view import CartAPI
from app.api.delivery_info_view import DeliveryInfoAPI
from app.api.menu_item_view import MenuItemAPI, MenuItemByResturantApi
from app.api.order_details_view import OrderDetailsAPI
from app.api.order_view import OrderAPI, OrderStatusApi, OrderResturantApi
from app.api.resturant_view import ResturantAPI, ResturantByUserApi
from app.api.rider_view import RiderAPI, RiderByUserApi
from app.api.user_view import UserAPI
from app.api.auth_view import LoginAPI, RegisterAPI



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
auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')


address_view = AddressAPI.as_view('address_api')
cartdetail_view = CartDetailsAPI.as_view('cartdetails_api')
cart_view = CartAPI.as_view('cart_api')
deiveryinfo_view = DeliveryInfoAPI.as_view('deliveryinfo_api')

# this is the route for menu item
menuitem_view = MenuItemAPI.as_view('menuitem_api')
menuitem_bp.add_url_rule('',defaults={'menu_item_id': None}, view_func=menuitem_view, methods=['GET'])
menuitem_bp.add_url_rule('', view_func=menuitem_view,methods=['POST'])
menuitem_bp.add_url_rule('/<int:menu_item_id>', view_func=menuitem_view, methods=['GET','PUT','DELETE'])

menuitem_by_resturant_view = MenuItemByResturantApi.as_view('menuitem_by_resturant')
menuitem_bp.add_url_rule('/resturant/<int:resturant_id>', view_func=menuitem_by_resturant_view,methods=['GET'])

#this is the route for order details
orderdetails_view = OrderDetailsAPI.as_view('orderdetails_api')

#this is the route for order
order_view = OrderAPI.as_view('order_api')
order_bp.add_url_rule('',defaults={'order_id':None}, view_func=order_view, methods=['GET'])
order_bp.add_url_rule('',view_func=order_view, methods=['POST'])
order_bp.add_url_rule('/<int:order_id>', view_func=order_view, methods=['GET','PUT','DELETE'])

order_status_view = OrderStatusApi.as_view('order_status_api')
order_bp.add_url_rule('/status',view_func=order_status_view, methods=['GET'])

order_resturant_view = OrderResturantApi.as_view('order_resturant_api')
order_bp.add_url_rule('/resturant',view_func=order_resturant_view, methods=['GET'])


# this is the route for resturant
resturant_view = ResturantAPI.as_view('resturant_api')
resturant_bp.add_url_rule('',defaults={'resturant_id':None}, view_func=resturant_view, methods=['GET'])
resturant_bp.add_url_rule('', view_func=resturant_view,methods=['POST'])
resturant_bp.add_url_rule('/<int:resturant_id>',view_func=resturant_view, methods=['GET','PUT','DELETE'])

resturant_by_user_view = ResturantByUserApi.as_view('resturant_by_user_api')
resturant_bp.add_url_rule('/user/<int:user_id>',view_func=resturant_by_user_view, methods=['GET'])

#this the route for rider
rider_view = RiderAPI.as_view('rider_api')
rider_bp.add_url_rule('',defaults={'rider_id':None}, view_func=rider_view, methods=['GET'])
rider_bp.add_url_rule('/<int:rider_id>',view_func=rider_view,methods=['GET','PUT','DELETE'])

rider_by_user_view = RiderByUserApi.as_view('rider_by_user_api')
rider_bp.add_url_rule('/user/<int:rider_id>', view_func=rider_by_user_view, methods=['GET'])

# this is the route for user
user_view = UserAPI.as_view('user_api')
user_bp.add_url_rule('',defaults={'user_id':None}, view_func=user_view, methods=['GET'])
user_bp.add_url_rule('', view_func=user_view, methods=['POST'])
user_bp.add_url_rule('/<int:user_id>', view_func=user_view, methods=['GET','PUT','DELETE'])

# this is the route for auth
login_view = LoginAPI.as_view('login_api')
register_view = RegisterAPI.as_view('register_api')
auth_bp.add_url_rule('/login', view_func=login_view, methods=['POST'])
auth_bp.add_url_rule('/register', view_func=register_view, methods=['POST'])

def register_routes(app):
    """function to register routes"""
    app.register_blueprint(address_bp, url_prefix='/address')
    app.register_blueprint(cartdetail_bp, url_prefix='/cart_details')
    app.register_blueprint(cart_bp, url_prefix='/cart')
    app.register_blueprint(deliveryinfo_bp, url_prefix='/delivery_info')
    app.register_blueprint(menuitem_bp, url_prefix='/menuitem')
    app.register_blueprint(orderdetail_bp, url_prefix='/order_details')
    app.register_blueprint(order_bp, url_prefix='/order')
    app.register_blueprint(resturant_bp, url_prefix='/resturant')
    app.register_blueprint(rider_bp, url_prefix='/rider')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(auth_bp, url_prefix='/auth')
