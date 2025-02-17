from flask import Blueprintmkd

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *  # noqa
