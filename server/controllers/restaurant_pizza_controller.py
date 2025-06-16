from flask import Blueprint, request, jsonify
from server.models import db, RestaurantPizza, Pizza, Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    errors = []

    # Validate price
    if not isinstance(price, int) or not (1 <= price <= 30):
        errors.append("Price must be between 1 and 30")

    # Validate pizza exists
    pizza = Pizza.query.get(pizza_id)
    if not pizza:
        errors.append("Pizza not found")

    # Validate restaurant exists
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        errors.append("Restaurant not found")

    if errors:
        return jsonify({"errors": errors}), 400

    # Create new RestaurantPizza
    new_rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)

    db.session.add(new_rp)
    db.session.commit()

    response = {
        "id": new_rp.id,
        "price": new_rp.price,
        "pizza_id": new_rp.pizza_id,
        "restaurant_id": new_rp.restaurant_id,
        "pizza": {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        },
        "restaurant": {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
    }

    return jsonify(response), 201
