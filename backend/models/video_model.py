from extensions.db import videos_collection
from bson import ObjectId


def get_active_videos():
    return list(videos_collection.find({"is_active": True}).limit(2))


def find_video_by_id(video_id):
    return videos_collection.find_one({"_id": ObjectId(video_id)})


