from flask import Blueprint, jsonify, request
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza

bp = Blueprint('restaurant_pizzas', __name__, url_prefix='/restaurant_pizzas')

@bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        price = data.get('price')
        restaurant_id = data.get('restaurant_id')
        pizza_id = data.get('pizza_id')

        if price is None or restaurant_id is None or pizza_id is None:
            raise ValueError('Missing required fields')

        rp = RestaurantPizza(
            price=price,
            restaurant_id=restaurant_id,
            pizza_id=pizza_id
        )
        db.session.add(rp)
        db.session.commit()

        return jsonify({
            'id': rp.id,
            'price': rp.price,
            'pizza_id': rp.pizza_id,
            'restaurant_id': rp.restaurant_id,
            'pizza': {
                'id': rp.pizza.id,
                'name': rp.pizza.name,
                'ingredients': rp.pizza.ingredients
            },
            'restaurant': {
                'id': rp.restaurant.id,
                'name': rp.restaurant.name,
                'address': rp.restaurant.address
            }
        }), 201
    except ValueError as ve:
        db.session.rollback()
        return jsonify({'errors': [str(ve)]}), 400
    except Exception:
        db.session.rollback()
        return jsonify({'errors': ['Invalid request']}), 400
