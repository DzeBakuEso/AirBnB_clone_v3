#!/usr/bin/python3
"""Initialize app_views Blueprint"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all view modules
from api.v1.views.states import *
