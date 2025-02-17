i#!/usr/bin/python3
"""Defines the API views for User objects."""
from flask import Flask, jsonify, request
from models import storage
from models.user import User
from flask import Blueprint

users = Blueprint('users', __name__)

@users.route('/users', methods=['GET'])
def get_all_users():
    """Handles GET requests for all User objects."""
    users = storage.all(User)
    return jsonify([user.to_dict() for user in users.values()])

@users.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Handles GET requests for a specific User object."""
    user = storage.get(User, user_id)
    if not user:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(user.to_dict())

@users.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Handles DELETE requests for a specific User object."""
    user = storage.get(User, user_id)
    if not user:
        return jsonify({'error': 'Not found'}), 404
    storage.delete(user)
    storage.save()
    return jsonify({}), 200

@users.route('/users', methods=['POST'])
def create_user():
    """Handles POST requests to create a User object."""
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    data = request.get_json()
    if 'email' not in data:
        return jsonify({'error': 'Missing email'}), 400
    if 'password' not in data:
        return jsonify({'error': 'Missing password'}), 400
    user = User(**data)
    storage.new(user)
    storage.save()
    return jsonify(user.to_dict()), 201

@users.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """Handles PUT requests to update a specific User object."""
    user = storage.get(User, user_id)
    if not user:
        return jsonify({'error': 'Not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict()), 200
i#!/usr/bin/python3
"""Defines the API views for User objects."""
from flask import Flask, jsonify, request
from models import storage
from models.user import User
from flask import Blueprint

users = Blueprint('users', __name__)

@users.route('/users', methods=['GET'])
def get_all_users():
    """Handles GET requests for all User objects."""
    users = storage.all(User)
    return jsonify([user.to_dict() for user in users.values()])

@users.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Handles GET requests for a specific User object."""
    user = storage.get(User, user_id)
    if not user:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(user.to_dict())

@users.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Handles DELETE requests for a specific User object."""
    user = storage.get(User, user_id)
    if not user:
        return jsonify({'error': 'Not found'}), 404
    storage.delete(user)
    storage.save()
    return jsonify({}), 200

@users.route('/users', methods=['POST'])
def create_user():
    """Handles POST requests to create a User object."""
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    data = request.get_json()
    if 'email' not in data:
        return jsonify({'error': 'Missing email'}), 400
    if 'password' not in data:
        return jsonify({'error': 'Missing password'}), 400
    user = User(**data)
    storage.new(user)
    storage.save()
    return jsonify(user.to_dict()), 201

@users.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """Handles PUT requests to update a specific User object."""
    user = storage.get(User, user_id)
    if not user:
        return jsonify({'error': 'Not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict()), 200

