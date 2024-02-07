from flask import Flask, jsonify, send_from_directory
from flask_pymongo import PyMongo
from flask_cors import CORS  # Import CORS
import os  # Import os module

from config import Config

# Initialize Flask app
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(Config)

# Initialize PyMongo for MongoDB connection
mongo = PyMongo(app)

# Enable CORS
CORS(app)

# Define the directory path for images
# IMAGE_DIRECTORY = os.path.join(app.root_path, 'images')

# Import routes and models (if any)
from api import overlays, livestream


@app.route('/api/logos')
def get_logos():
    logos = [
        {"id": 1, "url": "/static/logo.png"}
        # Add more logos as needed
    ]
    return jsonify(logos)


@app.route('/api/images/<path:image_filename>')
def get_image(image_filename):
    return send_from_directory(IMAGE_DIRECTORY, image_filename)

# Register Blueprint for API routes
app.register_blueprint(overlays.overlays_bp)
app.register_blueprint(livestream.livestream_bp)

if __name__ == "__main__":
    app.run(debug=True)

