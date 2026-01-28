import jwt
from datetime import datetime, timedelta
from config import Config

def generate_playback_token(video_id):
    payload = {
        "video_id": video_id,
        "exp": datetime.utcnow() + timedelta(minutes=10)
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")

def verify_playback_token(token):
    try:
        payload = jwt.decode(
            token,
            Config.SECRET_KEY,
            algorithms=["HS256"]
        )
        return payload["video_id"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
