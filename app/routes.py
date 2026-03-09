from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.gemini_generator import generate_workout_gemini
from app.gemini_flash_generator import generate_nutrition_tip_with_flash

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/generate-workout", response_class=HTMLResponse)
def generate_workout(
    request: Request,
    name: str = Form(...),
    age: int = Form(...),
    weight: float = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...)
):

    user_input = {
        "name": name,
        "age": age,
        "weight": weight,
        "goal": goal,
        "intensity": intensity
    }

    workout_plan = generate_workout_gemini(user_input)
    nutrition_tip = generate_nutrition_tip_with_flash(goal)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "plan": workout_plan,
            "tip": nutrition_tip,
            "name": name
        }
    )



@router.post("/submit-feedback", response_class=HTMLResponse)
async def submit_feedback(request: Request, feedback: str = Form("")):

    if feedback.strip() == "":
        return templates.TemplateResponse(
            "feedback_error.html",
            {"request": request}
        )

    return templates.TemplateResponse(
        "thankyou.html",
        {
            "request": request,
            "feedback": feedback
        }
    )

@router.get("/view-all-users", response_class=HTMLResponse)
def view_all_users(request: Request):

    users = [
        {
            "name": "Demo User",
            "age": 22,
            "weight": 70,
            "goal": "weight loss",
            "intensity": "medium",
            "plan": "Sample 7-day workout plan"
        }
    ]

    return templates.TemplateResponse(
        "all_users.html",
        {
            "request": request,
            "users": users
        }
    )
