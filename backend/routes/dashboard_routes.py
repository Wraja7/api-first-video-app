
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from models.video_model import get_active_videos



dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():
    videos = get_active_videos()

    return jsonify([
        {
            "id": str(v["_id"]),
            "title": v["title"],
            "description": v["description"],
            "thumbnail_url": v["thumbnail_url"]
        }
        for v in videos
    ]), 200

