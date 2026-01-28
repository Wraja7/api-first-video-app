from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["video_app"]

users_collection = db["users"]
videos_collection = db["videos"]
