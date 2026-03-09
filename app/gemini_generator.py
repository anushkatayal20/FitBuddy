import google.generativeai as genai

# configure API
genai.configure(api_key="AIzaSyDHFZOdFONawY65Xvfc5OcfVIIXTWyjH5")

# load model
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_workout_gemini(user_input):

    prompt = f"""
You are a professional fitness trainer.

Create a structured 7-day workout plan.

User goal: {user_input['goal']}
Workout intensity: {user_input['intensity']}

Each day must include:
Warm-up
Main Workout
Cooldown

Format:

Day 1:
Warm-up:
Main Workout:
Cooldown:

Repeat for Day 2 to Day 7.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:

        # fallback plan if API fails
        return """
Day 1:
Warm-up: Jumping jacks (5 minutes)
Main Workout: Push-ups (3 sets x 12 reps), Squats (3 x 15)
Cooldown: Full body stretching

Day 2:
Warm-up: Jogging (5 minutes)
Main Workout: Lunges (3 x 12), Plank (3 x 30 sec)
Cooldown: Deep breathing exercises

Day 3:
Warm-up: Arm circles + light jogging
Main Workout: Dumbbell rows (3 x 12), Shoulder press (3 x 10)
Cooldown: Shoulder and arm stretches

Day 4:
Warm-up: Brisk walking
Main Workout: Light yoga session and mobility exercises
Cooldown: Relaxation breathing

Day 5:
Warm-up: Jump rope (5 minutes)
Main Workout: Burpees (3 x 10), Mountain climbers (3 x 20)
Cooldown: Lower body stretching

Day 6:
Warm-up: Dynamic stretching
Main Workout: Step-ups (3 x 12), Bicycle crunches (3 x 15)
Cooldown: Core stretching

Day 7:
Warm-up: Light jogging
Main Workout: Full body circuit (push-ups, squats, plank)
Cooldown: Deep stretching and recovery breathing
"""
