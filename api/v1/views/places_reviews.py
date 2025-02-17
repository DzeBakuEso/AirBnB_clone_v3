#!/usr/bin/python3
"""Defines the API views for Review objects."""
from flask import Flask, jsonify, request
from models import storage
from models.review import Review
from models.place import Place
from models.user import User
from flask import Blueprint

reviews = Blueprint('reviews', __name__)

@reviews.route('/places/<place_id>/reviews', methods=['GET'])
def get_reviews_for_place(place_id):
    """Handles GET requests for all Review objects in a Place."""
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({'error': 'Not found'}), 404
    reviews = storage.all(Review)
    place_reviews = [review.to_dict() for review in reviews.values() if review.place_id == place.id]
    return jsonify(place_reviews)

@reviews.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    """Handles GET requests for a specific Review object."""
    review = storage.get(Review, review_id)
    if not review:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(review.to_dict())

@reviews.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    """Handles DELETE requests for a specific Review object."""
    review = storage.get(Review, review_id)
    if not review:
        return jsonify({'error': 'Not found'}), 404
    storage.delete(review)
    storage.save()
    return jsonify({}), 200

@reviews.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    """Handles POST requests to create a Review object in a Place."""
    place = storage.get(Place, place_id)
    if not place:
        return jsonify({'error': 'Not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    data = request.get_json()
    if 'user_id' not in data:
        return jsonify({'error': 'Missing user_id'}), 400
    user = storage.get(User, data['user_id'])
    if not user:
        return jsonify({'error': 'Not found'}), 404
    if 'text' not in data:
        return jsonify({'error': 'Missing text'}), 400
    review = Review(**data, place_id=place_id)
    storage.new(review)
    storage.save()
    return jsonify(review.to_dict()), 201

@reviews.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    """Handles PUT requests to update a specific Review object."""
    review = storage.get(Review, review_id)
    if not review:
        return jsonify({'error': 'Not found'}), 404
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'user_id', 'place_id', 'created_at', 'updated_at']:
            setattr(review, key, value)
    storage.save()
    return jsonify(review.to_dict()), 200
