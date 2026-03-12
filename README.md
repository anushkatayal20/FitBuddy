# FitBuddy AI Trainer

FitBuddy is an AI-powered fitness assistant that generates personalized 7-day workout plans based on a user's goal and workout intensity.

## Features

- AI generated workout plans
- Personalized nutrition tips
- Feedback-based workout plan updates
- Admin dashboard to view users and plans
- Modern UI with workout cards

## Tech Stack

- FastAPI
- Python
- Gemini AI
- SQLite
- HTML, CSS
- Jinja2 Templates

## Project Structure

fitbuddy/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── gemini_generator.py
│   ├── gemini_flash_generator.py
│   ├── updated_plan.py
│   ├── database.py
│
├── templates/
│   ├── index.html
│   ├── result.html
│   ├── all_users.html
│
├── static/
│   └── style.css
│
└── requirements.txt

## How to Run

1. Install dependencies

pip install -r requirements.txt

2. Run server

uvicorn app.main:app --reload

3. Open browser

http://127.0.0.1:8000

4.Check this out

https://fit-buddy--anamika98.replit.app
