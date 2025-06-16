# server/controllers/restaurant_pizza_controller.py

from flask import Blueprint, jsonify, request
from ..models.restaurant_pizza import RestaurantPizza
from ..models.pizza import Pizza
from ..models.restaurant import Restaurant
from ..app import db

restaurant_pizza_bp = Blueprint("restaurant_pizzas", __name__)

@restaurant_pizza_bp.route("/", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()

    try:
        price = int(data["price"])
        pizza_id = int(data["pizza_id"])
        restaurant_id = int(data["restaurant_id"])
    except (KeyError, ValueError, TypeError):
        return jsonify({"errors": ["Invalid input format"]}), 400

    rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)

    if not rp.is_valid_price():
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    db.session.add(rp)
    db.session.commit()

    return jsonify(rp.to_dict()), 201
