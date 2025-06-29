"""seed class to add data """
from app import create_app
from datetime import datetime
from app.extensions import db
from app.models import (
    User, Rider, Resturant, MenuItem,
    Address, Cart, CartDetails,
    Order, OrderDetails, DeliveryInfo
)

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # --- USERS ---
    user1 = User(name="Ali", email="ali@example.com", password="pass123", phone="03001234567")
    user2 = User(name="Fatima", email="fatima@example.com", password="pass456", phone="03121234567")
    db.session.add_all([user1, user2])
    db.session.flush()  # Flush to get user_id

    # --- ADDRESSES ---
    address1 = Address(user_id=user1.user_id, street="Street 1", city="Karachi", state="Sindh",
                       zip_code="74000", latitude=24.8607, longitude=67.0011)
    address2 = Address(user_id=user2.user_id, street="Street 2", city="Lahore", state="Punjab",
                       zip_code="54000", latitude=31.5497, longitude=74.3436)
    db.session.add_all([address1, address2])

    # --- RIDERS ---
    rider1 = Rider(name="Rashid", phone="03451234567", vehicle_type="Bike",
                   current_location_lat=24.8607, current_location_lng=67.0011, is_available=True)
    db.session.add(rider1)
    db.session.flush()

    # --- RESTAURANTS ---
    rest1 = Resturant(name="Burger Hub", address="123 Main St", logo_url="http://example.com/logo1.png",
                      phone="02112345678", rating=4.5, open_hours="10:00 AM - 11:00 PM")
    db.session.add(rest1)
    db.session.flush()

    # --- MENU ITEMS ---
    item1 = MenuItem(name="Zinger Burger", description="Spicy chicken burger", price=550,
                     image_url="http://example.com/zinger.png", is_available=True,
                     resturant_id=rest1.resturant_id)
    item2 = MenuItem(name="Fries", description="Crispy fries", price=200,
                     image_url="http://example.com/fries.png", is_available=True,
                     resturant_id=rest1.resturant_id)
    db.session.add_all([item1, item2])
    db.session.flush()

    # --- CARTS ---
    cart1 = Cart(user_id=user1.user_id, status="active")
    db.session.add(cart1)
    db.session.flush()

    # --- CART DETAILS ---
    cart_detail1 = CartDetails(cart_id=cart1.cart_id, menuitem_id=item1.menuitem_id, quantity="2")
    cart_detail2 = CartDetails(cart_id=cart1.cart_id, menuitem_id=item2.menuitem_id, quantity="1")
    db.session.add_all([cart_detail1, cart_detail2])

    # --- ORDERS ---
    order1 = Order(user_id=user1.user_id, address_id=address1.address_id, rider_id=rider1.rider_id,
                   resturant_id=rest1.resturant_id, total_price=1300.0,
                   status="preparing", created_at=datetime.utcnow())
    db.session.add(order1)
    db.session.flush()

    # --- ORDER DETAILS ---
    od1 = OrderDetails(order_id=order1.order_id, menuitem_id=item1.menuitem_id,
                       quantity=2, unit_price=item1.price)
    od2 = OrderDetails(order_id=order1.order_id, menuitem_id=item2.menuitem_id,
                       quantity=1, unit_price=item2.price)
    db.session.add_all([od1, od2])

    # --- DELIVERY INFO ---
    delivery_info = DeliveryInfo(order_id=order1.order_id, rider_id=rider1.rider_id,
                                 pickup_time=datetime.utcnow(), delivery_time=datetime.utcnow(),
                                 status="picked")
    db.session.add(delivery_info)

    # --- COMMIT ---
    db.session.commit()
    print("✅ Full database seeded successfully!")
