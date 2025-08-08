"""admin dashboard"""
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from wtforms_sqlalchemy.fields import QuerySelectField

from .extensions import db
from .models.address import Address
from .models.cart_details import CartDetails
from .models.cart import Cart
from .models.delivery_info import DeliveryInfo
from .models.menu_item import MenuItem
from .models.order_details import OrderDetails
from .models.order import Order
from .models.resturant import Resturant
from .models.rider import Rider
from .models.user import User

admin = Admin(name="Admin Dashboard", template_mode="bootstrap3")


class RestaurantAdmin(ModelView):
    """class for resturant view"""
    form_columns = [
        'name', 'address','latitude','longitude', 'logo_url', 'phone',
        'rating', 'tags', 'open_hours', 'user_id'
    ]
    column_list = [
        'resturant_id', 'name', 'user_id', 'address','latitude','longitude', 'logo_url', 'phone',
        'rating', 'tags', 'open_hours',
    ]
    column_display_pk = True

class OrderAdmin(ModelView):
    """class for resturant view"""
    form_columns = [
    ]
    column_list = [
        'order_id', 'user_id', 'address_id', 'rider_id',
        'resturant_id', 'total_price', 'status', 'payment_method', 'created_at'
    ]
    column_display_pk = True

class RiderAdmin(ModelView):
    """class for rider view"""
    form_columns = [
        'name', 'phone','vehicle_type',
        'current_location_lat', 'current_location_lng', 'is_available'
    ]
    column_list = [
        'rider_id','name', 'phone','vehicle_type', 'license_number',
        'current_location_lat', 'current_location_lng', 'is_available'
    ]
    column_display_pk = True

class MenuItemAdmin(ModelView):
    """class for resturant view"""
    form_columns = [
        'name', 'description', 'price', 'image_url',
        'is_available'
    ]
    column_list = [
        'menuitem_id','resturant_id','name', 'description', 'price', 'image_url',
        'is_available',
    ]
    column_display_pk = True

class OrderDetailsAdmin(ModelView):
    """class for resturant view"""
    form_columns = [
        'orderdetails_id', 'order_id', 'menuitem_id', 'quantity',
        'unit_price'
    ]
    column_list = [
        'orderdetails_id', 'order_id', 'menuitem_id', 'quantity',
        'unit_price'
    ]
    column_display_pk = True
    
class AddressAdmin(ModelView):
    """class for resturant view"""
    form_columns = [
        'address_id', 'user_id', 'street', 'city',
        'state','zip_code','latitude','longitude'
    ]
    column_list = [
        'address_id', 'user_id', 'street', 'city',
        'state','zip_code','latitude','longitude'
    ]
    column_display_pk = True

def init_admin(app):
    """initialize function for admin dashboard"""
    admin.init_app(app)
    admin.add_view(AddressAdmin(Address, db.session))
    admin.add_view(ModelView(CartDetails, db.session))
    admin.add_view(ModelView(Cart,db.session))
    admin.add_view(ModelView(DeliveryInfo,db.session))
    admin.add_view(MenuItemAdmin(MenuItem, db.session))
    admin.add_view(OrderDetailsAdmin(OrderDetails, db.session))
    admin.add_view(OrderAdmin(Order, db.session))
    admin.add_view(RestaurantAdmin(Resturant, db.session))
    admin.add_view(RiderAdmin(Rider, db.session))
    admin.add_view(ModelView(User, db.session))
