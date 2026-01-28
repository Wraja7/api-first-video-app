from backend.extensions.db import db

videos = [
    {
        "title": "How Startups Fail",
        "description": "Lessons from real founders",
        "youtube_id": "9vJRopau0g0",
        "thumbnail_url": "https://img.youtube.com/vi/9vJRopau0g0/hqdefault.jpg",
        "is_active": True
    },
    {
        "title": "How to Build Products Users Love",
        "description": "Product thinking explained",
        "youtube_id": "FG1Fa-t4AEQ",
        "thumbnail_url": "https://img.youtube.com/vi/FG1Fa-t4AEQ/hqdefault.jpg",
        "is_active": True
    }
]

if __name__ == "__main__":
    db.videos.insert_many(videos)
    print("✅ Videos seeded successfully")
