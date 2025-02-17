from flask import jsonify, request
from models import storage
from models.city import City
from models.state import State
from api.v1.views import app_views
from werkzeug.exceptions import NotFound, BadRequest

@app_views.route('/states/<state_id>/cities', methods=['GET'])
def get_cities_by_state(state_id):
    """Retrieve a list of all City objects linked to a State."""
    state = storage.get(State, state_id)
    if not state:
        raise NotFound("State not found")
    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)

@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """Retrieve a specific City object."""
    city = storage.get(City, city_id)
    if not city:
        raise NotFound("City not found")
    return jsonify(city.to_dict())

@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """Delete a City object."""
    city = storage.get(City, city_id)
    if not city:
        raise NotFound("City not found")
    storage.delete(city)
    storage.save()
    return jsonify({})

@app_views.route('/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    """Create a new City."""
    state = storage.get(State, state_id)
    if not state:
        raise NotFound("State not found")
    
    if not request.is_json:
        raise BadRequest("Not a JSON")
    
    data = request.get_json()
    if 'name' not in data:
        raise BadRequest("Missing name")
    
    new_city = City(name=data['name'], state_id=state.id)
    storage.new(new_city)
    storage.save()
    return jsonify(new_city.to_dict()), 201

@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """Update an existing City object."""
    city = storage.get(City, city_id)
    if not city:
        raise NotFound("City not found")
    
    if not request.is_json:
        raise BadRequest("Not a JSON")
    
    data = request.get_json()
    for key, value in data.items():
        if key not in ["id", "state_id", "created_at", "updated_at"]:
            setattr(city, key, value)
    
    storage.save()
    return jsonify(city.to_dict())
