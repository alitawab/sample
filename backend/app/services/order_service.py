"""order service"""
from app.models.order import Order
from app.models.order_details import OrderDetails
from app.models.address import Address
from app.extensions import db
from sqlalchemy import or_
import requests


def get_all_orders():
    """get all order"""
    return Order.query.all()

def get_order(order_id):
    """get order"""
    return Order.query.get(order_id)

def get_order_by_resturant(resturant_id):
    """get order"""
    return Order.query.filter(Order.resturant_id == resturant_id).all()


def get_order_by_rider(rider_id):
    """get order"""
    return Order.query.filter(Order.rider_id == rider_id)


def get_order_by_status(statuses,rider_id=None):
    """Filter orders based on rider state"""
    query = Order.query

    if rider_id:
        ongoing_order = Order.query.filter(
            Order.rider_id == rider_id,
            Order.status != "Delivered"
        ).first()

        if ongoing_order:
            return [ongoing_order]
        else:
            query = query.filter(
                Order.status.in_(statuses),
                Order.status == "Accepted",
                Order.rider_id.is_(None)
            )
            return query.all()

    return []

def create_order(data):
    """create order"""
    address_data = data.pop('address')
    lat = address_data['latitude']
    lng = address_data['longitude']
    user_id = data.get("user_id")
    geo_data = reverse_geocode(lat,lng)

    print(data)
    address = Address(
        user_id=user_id,
        street=address_data["text"],
        city=geo_data["city"],
        state=geo_data["state"],
        zip_code=geo_data["zip_code"],
        latitude=lat,
        longitude=lng
    )
    db.session.add(address)
    db.session.flush()

    items = data.pop('items')
    order = Order(address_id=address.address_id, **data)
    db.session.add(order)
    db.session.flush()

    for item in items:
        order_details = OrderDetails(
            order_id=order.order_id,
            menuitem_id=item['menuitem_id'],
            quantity=item['quantity'],
            unit_price=item['unit_price']
        )
        db.session.add(order_details)

    db.session.commit()
    return order

def update_order(order, data):
    """update order"""
    for key, value in data.items():
        setattr(order, key, value)
    db.session.commit()
    return order

def delete_order(order):
    """delete order"""
    db.session.delete(order)
    db.session.commit()


# def accept_order(order_id):
#     order = get_order(order_id)
#     if order and order.status == OrderStatus.PENDING:
#         order.status = OrderStatus.PREPARING
#         db.session.commit()
#     return order

# def mark_ready(order_id):
#     order = get_order(order_id)
#     if order and order.status == OrderStatus.PREPARING:
#         order.status = OrderStatus.READY_FOR_PICKUP
#         db.session.commit()
#     return order

# def assign_rider(order_id, rider_id):
#     order = get_order(order_id)
#     if order and order.status == OrderStatus.PREPARING:
#         order.rider_id = rider_id
#         db.session.commit()
#     return order

# def pickup_order(order_id):
#     order = get_order(order_id)
#     if order and order.status == OrderStatus.READY_FOR_PICKUP:
#         order.status = OrderStatus.OUT_FOR_DELIVERY
#         db.session.commit()
#     return order

# def complete_order(order_id):
#     order = get_order(order_id)
#     if order and order.status == OrderStatus.OUT_FOR_DELIVERY:
#         order.status = OrderStatus.COMPLETED
#         db.session.commit()
#     return order

def reverse_geocode(lat,lng):
    """function to collect cuty zip code street from latitude and longitude"""
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {
        "format":"json",
        "lat":lat,
        "lon":lng,
        "zoom":18,
        "addressdetails":1
    }
    headers = {
        "User-Agent":"reverse-geocoder-script/0.1 (ali.tawab92@gmail.com)"
    }

    response = requests.get(url, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json().get("address",{})

    return {
        "street":data.get("road",""),
        "city":data.get("city") or data.get("town") or data.get("village",""),
        "state": data.get("state",""),
        "zip_code": data.get("postcode","")
    }
