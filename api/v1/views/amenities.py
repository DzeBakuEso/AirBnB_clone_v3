#!/usr/bin/python3
"""Defines the API views for Amenity objects."""
from flask import Flask, jsonify, request
from models import storage
from models.amenity import Amenity
from flask import Blueprint

amenities = Blueprint('amenities', __name__)

@amenities.route('/amenities', methods=['GET'])
def get_all_amenities():
    """Handles GET requests for all Amenity objects."""
    amenities = storage.all(Amenity)
    return jsonify([amenity.to_dict() for amenity in amenities.values()])

@amenities.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """Handles GET requests for a specific Amenity object."""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(amenity.to_dict())

@amenities.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    """Handles DELETE requests for a specific Amenity object."""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        return jsonify({'error': 'Not found'}), 404
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200

@amenities.route('/amenities', methods=['POST'])
def create_amenity():
    """Handles POST requests to create an Amenity object."""
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Missing name'}), 400
    amenity = Amenity(**data)
    storage.new(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201

@amenities.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """Handles PUT requests to update a specific Amenity object."""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        return jsonify({'error': 'Not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200
