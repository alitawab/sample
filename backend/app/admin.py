"""admin dashboard"""
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .extensions import db
from .models import Address, CartDetails,Cart,DeliveryInfo,MenuItem,OrderDetails,Order,Resturant,Rider,User


admin = Admin(name="Admin Dashboard", template_mode="bootstrap3")

def init_admin(app):
    """initialize function for admin dashboard"""
    admin.init_app(app)
    admin.add_view(ModelView(Address, db.session))
    admin.add_view(ModelView(CartDetails, db.session))
    admin.add_view(ModelView(Cart,db.session))
    admin.add_view(ModelView(DeliveryInfo,db.session))
    admin.add_view(ModelView(MenuItem, db.session))
    admin.add_view(ModelView(OrderDetails, db.session))
    admin.add_view(ModelView(Order, db.session))
    admin.add_view(ModelView(Resturant, db.session))
    admin.add_view(ModelView(Rider, db.session))
    admin.add_view(ModelView(User, db.session))
