from flask import Blueprint, request, jsonify
from flask_pymongo import ObjectId

from app import mongo

overlays_bp = Blueprint('overlays', __name__, url_prefix='/api/overlays')

# Endpoint to create a new overlay
@overlays_bp.route('/create', methods=['POST'])
def create_overlay():
    data = request.json
    overlay = {
        'type': data['type'],
        'content': data['content'],
        'position': data['position'],
        'size': data['size']
    }
    inserted_id = mongo.db.overlays.insert_one(overlay).inserted_id
    return jsonify({'message': 'Overlay created successfully', 'overlay_id': str(inserted_id)}), 201

# Endpoint to update an existing overlay
@overlays_bp.route('/update/<overlay_id>', methods=['PUT'])
def update_overlay(overlay_id):
    data = request.json
    updated_overlay = {
        'type': data['type'],
        'content': data['content'],
        'position': data['position'],
        'size': data['size']
    }
    mongo.db.overlays.update_one({'_id': ObjectId(overlay_id)}, {'$set': updated_overlay})
    return jsonify({'message': 'Overlay updated successfully'}), 200

# Endpoint to delete an existing overlay
@overlays_bp.route('/delete/<overlay_id>', methods=['DELETE'])
def delete_overlay(overlay_id):
    mongo.db.overlays.delete_one({'_id': ObjectId(overlay_id)})
    return jsonify({'message': 'Overlay deleted successfully'}), 200

# Endpoint to fetch all overlays
@overlays_bp.route('/all', methods=['GET'])
def get_all_overlays():
    overlays = list(mongo.db.overlays.find())
    for overlay in overlays:
        overlay['_id'] = str(overlay['_id'])
    return jsonify(overlays), 200
