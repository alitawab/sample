"""order service"""
from math import radians,sin,cos,asin,sqrt
import requests
from app.models.order import Order
from app.models.order_details import OrderDetails
from app.models.address import Address
from app.extensions import db
from app.services.rider_service import get_rider


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

    if rider_id:
        ongoing_order = Order.query.filter(
            Order.rider_id == rider_id,
            Order.status != "Delivered"
        ).first()

        if ongoing_order:
            return [ongoing_order]


        return get_available_order_for_rider(rider_id, statuses)

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

def get_available_order_for_rider(rider_id, statuses, max_distance_km=5):
    """function to get available rider close to resturant"""
    rider = get_rider(rider_id)
    if not rider:
        return[]
    available_orders = Order.query.filter(Order.status.in_(statuses), Order.rider_id.is_(None)).all()
    filtered_orders = []

    for order in available_orders:
        rest_lat = order.resturant.latitude
        rest_lng = order.resturant.longitude


        dist  = haversine_distance(
            rider.current_location_lat, rider.current_location_lng, rest_lat, rest_lng
            )

        if dist <= max_distance_km:
            filtered_orders.append(order)

    return filtered_orders


def haversine_distance(lat1,lng1,lat2,lng2):
    """function to calculat distance between rider and resturant"""
    r = 6371 #Earth Radius

    d_lat = radians(lat2-lat1)
    d_lng = radians(lng2-lng1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(d_lat/2) **2 + cos(lat1) * cos(lat2) *sin(d_lng/2)**2
    c = 2*asin(sqrt(a))

    return r * c
