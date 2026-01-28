from extensions.db import users_collection
from datetime import datetime
from bson import ObjectId


def create_user(name, email, password_hash):
    user = {
        "name": name,
        "email": email,
        "password_hash": password_hash,
        "created_at": datetime.utcnow(),
    }
    users_collection.insert_one(user)
    return user


def find_user_by_email(email):
    return users_collection.find_one({"email": email})


def find_user_by_id(user_id):
    return users_collection.find_one({"_id": ObjectId(user_id)})




