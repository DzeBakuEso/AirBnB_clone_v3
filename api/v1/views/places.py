i#!/usr/bin/python3
"""Defines the API views for Place objects."""
from flask import Flask, jsonify, request
from models import storage
from models.place import Place
from models.city import City
from models.user import User
from flask import Blueprint

places = Blueprint('places', __name__)

@places.route('/cities/<city_id>/places', methods=['GET'])
def get_places_in_city(city_id):
    """Handles GET requests for all Place objects in a City."""
    city = storage.get(City, city_id)
    if not city:
        return jsonify({'error': 'Not found'}), 404
    places = storage.all(Place)
    city_places = [place.to_dict() for place in places.values() if place.city_id == city.id]
    return jsonify(city_places)

@places.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    """Handles GET requests for a specific Place object."""
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(place.to_dict())

@places.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    """Handles DELETE requests for a specific Place object."""
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({'error': 'Not found'}), 404
    storage.delete(place)
    storage.save()
    return jsonify({}), 200

@places.route('/cities/<city_id>/places', methods=['POST'])
def create_place(city_id):
    """Handles POST requests to create a Place object in a City."""
    city = storage.get(City, city_id)
    if not city:
        return jsonify({'error': 'Not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    data = request.get_json()
    if 'user_id' not in data:
        return jsonify({'error': 'Missing user_id'}), 400
    user = storage.get(User, data['user_id'])
    if not user:
        return jsonify({'error': 'Not found'}), 404
    if 'name' not in data:
        return jsonify({'error': 'Missing name'}), 400
    place = Place(**data, city_id=city_id)
    storage.new(place)
    storage.save()
    return jsonify(place.to_dict()), 201

@places.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    """Handles PUT requests to update a specific Place object."""
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({'error': 'Not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    storage.save()
    return jsonify(place.to_dict()), 200
i#!/usr/bin/python3
"""Defines the API views for Place objects."""
from flask import Flask, jsonify, request
from models import storage
from models.place import Place
from models.city import City
from models.user import User
from flask import Blueprint

places = Blueprint('places', __name__)

@places.route('/cities/<city_id>/places', methods=['GET'])
def get_places_in_city(city_id):
    """Handles GET requests for all Place objects in a City."""
    city = storage.get(City, city_id)
    if not city:
        return jsonify({'error': 'Not found'}), 404
    places = storage.all(Place)
    city_places = [place.to_dict() for place in places.values() if place.city_id == city.id]
    return jsonify(city_places)

@places.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    """Handles GET requests for a specific Place object."""
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(place.to_dict())

@places.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    """Handles DELETE requests for a specific Place object."""
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({'error': 'Not found'}), 404
    storage.delete(place)
    storage.save()
    return jsonify({}), 200

@places.route('/cities/<city_id>/places', methods=['POST'])
def create_place(city_id):
    """Handles POST requests to create a Place object in a City."""
    city = storage.get(City, city_id)
    if not city:
        return jsonify({'error': 'Not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    data = request.get_json()
    if 'user_id' not in data:
        return jsonify({'error': 'Missing user_id'}), 400
    user = storage.get(User, data['user_id'])
    if not user:
        return jsonify({'error': 'Not found'}), 404
    if 'name' not in data:
        return jsonify({'error': 'Missing name'}), 400
    place = Place(**data, city_id=city_id)
    storage.new(place)
    storage.save()
    return jsonify(place.to_dict()), 201

@places.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    """Handles PUT requests to update a specific Place object."""
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({'error': 'Not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    storage.save()
    return jsonify(place.to_dict()), 200
