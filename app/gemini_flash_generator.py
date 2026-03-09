import google.generativeai as genai

# configure API
genai.configure(api_key="AIzaSyDHFZOdFONawY65Xvfc5OcfVIIXTWyjH5")

# load flash model
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_nutrition_tip_with_flash(goal: str) -> str:

    prompt = f"""
You are a fitness nutrition expert.

Give ONE short and practical nutrition or recovery tip
for someone whose fitness goal is: {goal}.

Keep the answer under 20 words.
"""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception:

        # fallback tips if API fails
        if goal == "weight loss":
            return "Focus on high-protein and fiber-rich foods to stay full and support fat loss."

        elif goal == "muscle gain":
            return "Consume a protein-rich meal within 30 minutes after workouts to support muscle recovery."

        else:
            return "Stay hydrated and maintain a balanced diet with carbs, protein, and healthy fats."
        