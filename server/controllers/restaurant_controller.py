from flask import Blueprint, jsonify
from server.models import Restaurant

restaurant_bp = Blueprint('restaurants', __name__, url_prefix='/restaurants')

@restaurant_bp.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()

    # Serialize restaurants to JSON-friendly dict
    restaurants_list = [{
        "id": r.id,
        "name": r.name,
        "address": r.address
    } for r in restaurants]

    return jsonify(restaurants_list), 200
