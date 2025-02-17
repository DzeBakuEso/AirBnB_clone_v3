#!/usr/bin/python3
"""API entry point"""

from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)

@app.errorhandler(404)
def not_found(error):
    """Returns a JSON-formatted 404 status code response"""
    return jsonify({"error": "Not found"}), 404

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
