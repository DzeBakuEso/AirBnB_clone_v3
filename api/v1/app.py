#!/usr/bin/python3
"""Flask app that initializes the API and handles routes."""
from flask import Flask
from flask_cors import CORS
from api.v1.views import app_views
from models import storage
from flask import jsonify

app = Flask(__name__)

# Enable CORS for all routes and all domains during development
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

# Register blueprint for API views
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """Closes the current SQLAlchemy session."""
    storage.close()

@app.errorhandler(404)
def page_not_found(error):
    """Handles 404 errors and returns a JSON response."""
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
