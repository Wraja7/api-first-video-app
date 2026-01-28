from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from models.video_model import find_video_by_id



video_bp = Blueprint("video", __name__, url_prefix="/video")

@video_bp.route("/<video_id>/stream", methods=["GET"])
@jwt_required()
def stream_video(video_id):
    video = find_video_by_id(video_id)

    if not video:
        return jsonify({"error": "Video not found"}), 404

    # OPTION A (allowed): embed-safe URL
    stream_url = f"https://www.youtube.com/embed/{video['youtube_id']}"

    return jsonify({ "stream_url": stream_url }), 200



