#!/usr/bin/python3
"""Initialize the API views."""
from flask import Blueprint
from api.v1.views.places import places

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Register blueprints for all views
app_views.register(places)
