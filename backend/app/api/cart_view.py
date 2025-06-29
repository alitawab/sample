from flask.views import MethodView
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from app.models import Cart, User, MenuItem, CartDetails
from app.extensions import db

class CartAPI(MethodView):
    def get(self):
        """Create or get cart for authenticated or guest user"""
        verify_jwt_in_request(optional=True)
        user_id = get_jwt_identity()

        if user_id:
            user = User.query.get(user_id)
            if not user:
                return jsonify({"error": "User not found"}), 404
        else:
            data = request.get_json()
            if not data:
                return jsonify({"error": "Guest data required"}), 400

            email = data.get("email")
            name = data.get("name", "Guest")
            phone = data.get("phone", "")

            if not email:
                return jsonify({"error": "Email is required for guest checkout"}), 400

            user = User.query.filter_by(email=email).first()

            if not user:
                user = User(name=name, email=email, password="", phone=phone)
                db.session.add(user)
                db.session.commit()

        cart = Cart.query.filter_by(user_id=user.user_id, status="active").first()
        if not cart:
            cart = Cart(user_id=user.user_id, status="active")
            db.session.add(cart)
            db.session.commit()

        return jsonify({
            "message": "Cart is ready",
            "cart_id": cart.cart_id,
            "user_id": user.user_id
        }), 200


class CartItemAPI(MethodView):
    def post(self):
        """Add item to cart"""
        data = request.get_json()

        verify_jwt_in_request(optional=True)
        user_id = get_jwt_identity()

        if not user_id:
            email = data.get("email")
            if not email:
                return jsonify({"error": "Email is required"}), 400
            user = User.query.filter_by(email=email).first()
            if not user:
                return jsonify({"error": "Guest user not found"}), 400
            user_id = user.user_id

        cart = Cart.query.filter_by(user_id=user_id, status="active").first()
        if not cart:
            return jsonify({"error": "Cart not found"}), 404

        menuitem_id = data.get("menuitem_id")
        quantity = data.get("quantity", 1)

        if not menuitem_id or quantity <= 0:
            return jsonify({"error": "Invalid menu item or quantity"}), 400

        menu_item = MenuItem.query.get(menuitem_id)
        if not menu_item or not menu_item.is_available:
            return jsonify({"error": "Menu item is not available"}), 404

        cart_item = CartDetails.query.filter_by(
            cart_id=cart.cart_id,
            menuitem_id=menuitem_id
        ).first()

        if cart_item:
            cart_item.quantity = str(int(cart_item.quantity) + quantity)
            message = "Item updated"
        else:
            cart_item = CartDetails(
                cart_id=cart.cart_id,
                menuitem_id=menuitem_id,
                quantity=str(quantity)
            )
            db.session.add(cart_item)
            message = "Item added"

        db.session.commit()

        return jsonify({
            "message": message,
            "cart_id": cart.cart_id,
            "item": {
                "menuitem_id": menuitem_id,
                "quantity": cart_item.quantity
            }
        }), 200
