from typing import Any
# from crypt import methods
from flask import Flask, request, jsonify,abort
import pymongo
from pymongo import MongoClient 
# from flask import Markup
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Initialize Flask app
app = Flask(__name__)

# Enable CORS
CORS(app)

# Set up the MongoDB connection using environment variable
mongo_uri = os.getenv('MONGO_URI')

# Set up MongoDB connection
cluster = MongoClient(mongo_uri)
db = cluster['easy']
col = db['go']


@app.route('/api/overlays/create', methods=['POST'])
def create_overlay():
    try:
        data = request.json
        print("Received data:", data)  # Debugging statement

        overlay = {
            'id': data['id'],
            'type': data['type'],
            'content': data['content'],
            'size': data['size'],
            'position': data['position'],
        }
        print("Overlay:", overlay)  # Debugging statement
        inserted_id = col.insert_one(overlay)
        print("Inserted ID:", inserted_id)  # Debugging statement

        return jsonify({'message': 'Overlay created successfully', 'overlay_id': str(inserted_id)}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@app.route('/all', methods=['GET'])
def get_all_overlays():
    overlays = list(col.find())
    for overlay in overlays:
        overlay['_id'] = str(overlay['_id'])
    return jsonify(overlays), 200


@app.route('/delete', methods=['DELETE'])
def delete_overlay():
    try:
        data = request.json
        overlay_id = data.get('id')  # Get the overlay ID from the request body

        if overlay_id is None:
            abort(400, description="ID is missing in the request body")

        result = col.delete_one({'id': overlay_id})  # Use the 'id' field for deletion
        if result.deleted_count > 0:
            return jsonify({'message': 'Overlay deleted successfully'}), 200
        else:
            return jsonify({'message': 'Overlay not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/update', methods=['PUT'])
def update_overlay():
    try:
        data = request.json
        overlay_id = data.get('id')  # Get the overlay ID from the request body

        if overlay_id is None:
            abort(400, description="ID is missing in the request body")

        # Extract the fields to be updated from the request JSON
        update_data = {
            'type': data.get('type'),
            'content': data.get('content'),
            'size': data.get('size'),
            'position': data.get('position')
        }

        # Remove any None values from the update_data
        update_data = {k: v for k, v in update_data.items() if v is not None}

        if not update_data:
            return jsonify({'message': 'No update data provided'}), 400

        # Perform the update operation
        result = col.update_one({'id': overlay_id}, {'$set': update_data})

        if result.matched_count > 0:
            return jsonify({'message': 'Overlay updated successfully'}), 200
        else:
            return jsonify({'message': 'Overlay not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
   

if __name__ == "__main__":
    app.run(debug=True)
