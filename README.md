# API-First Video App 🎬

A React Native (Expo) application built using an **API-first architecture**, powered by a **Flask backend** and **MongoDB**.  
The mobile app acts as a thin client and contains **no business logic**.

---

## 🧱 Architecture (Non-Negotiable)

React Native App → Flask API → MongoDB  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;YouTube (hidden behind backend)

> ⚠️ The frontend never accesses YouTube directly.

---

## 📱 Mobile App (Expo + React Native)

### Responsibilities
- Call APIs only
- Store JWT securely
- Render backend data
- Send user actions

❌ No business logic  
❌ No hardcoded content  
❌ No YouTube URLs

---

### Screens Implemented

#### 1️⃣ Authentication
- **Signup**
  - Name
  - Email
  - Password
- **Login**
  - Email
  - Password
- On success:
  - JWT stored securely
  - Redirect to Dashboard

---

#### 2️⃣ Dashboard
- Fetches **exactly 2 videos** from backend
- Displays:
  - Thumbnail
  - Title
  - Short description
- Clicking a tile opens Video Player

---

#### 3️⃣ Video Player
- Plays video using backend-provided stream
- Controls:
  - Play / Pause
  - Seek bar
  - Mute / Unmute
- YouTube URL is never exposed

---

#### 4️⃣ Settings
- Shows user name & email
- Logout clears JWT and redirects to login

---

## 🧠 Backend (Flask + MongoDB)

### Authentication (JWT)
| Method | Endpoint | Description |
|------|--------|------------|
| POST | /auth/signup | Register user |
| POST | /auth/login | Login |
| GET | /auth/me | Get user profile |
| POST | /auth/logout | Mock logout |

- Passwords are **hashed**
- JWT used for protected routes

---

### Video System
Video documents stored as:
```json
{
  "title": "How Startups Fail",
  "description": "Lessons from real founders",
  "youtube_id": "abc123xyz",
  "thumbnail_url": "...",
  "is_active": true
}
Method	Endpoint	Description
GET	/dashboard	Returns 2 active videos
GET	/video/<id>/stream	Returns playable stream
🔐 YouTube Abstraction Strategy
The backend never exposes raw YouTube URLs.

Instead:

Backend maps youtube_id → embed-safe stream

Frontend only consumes backend stream endpoint

This enforces:

Security

Abstraction

API ownership

🗃 Database Models
User
id

name

email

password_hash

created_at

Video
id

title

description

youtube_id

thumbnail_url

is_active

⚙️ Setup Instructions
Backend
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python seed_videos.py
python app.py
Frontend
cd mobile
npm install
npx expo start
📦 Environment Variables
Create .env using .env.example

🤖 AI Usage Disclosure
AI was used to:

Speed up boilerplate

Debug integration issues

AI outputs were reviewed, corrected, and adapted manually where incorrect.

Author

Raja Verma
