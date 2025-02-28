import json
import random

# Load the workout data from a JSON file
with open("organized_subcategories_v3.json", "r") as file:
    data = json.load(file)  # Use json.load() to read from a file

def get_random_exercises(category, type_, level, count=3):
    """
    Get random exercises from the data based on category, type (push, pull, legs), and level.
    """
    try:
        exercises = data['strength'][category][type_][level]
        return random.sample(exercises, min(count, len(exercises)))
    except KeyError:
        return []

def generate_sets_and_reps(category, intensity, goal):
    """
    Generate sets and reps dynamically based on category, intensity, and goal.

    Args:
        category (str): The exercise category (e.g., chest, shoulders, legs).
        intensity (str): The intensity level (e.g., beginner, intermediate, expert).
        goal (str): The training goal (e.g., strength, hypertrophy, endurance).

    Returns:
        dict: Recommended sets and reps.
    """
    if goal == "strength":
        if category in ["chest", "back", "legs"]:  # Compound movements
            if intensity == "beginner":
                return {"sets": 3, "reps": "6-8"}
            elif intensity == "intermediate":
                return {"sets": 4, "reps": "4-6"}
            elif intensity == "expert":
                return {"sets": 5, "reps": "3-5"}
        else:  # Isolation movements
            if intensity == "beginner":
                return {"sets": 3, "reps": "8-10"}
            elif intensity == "intermediate":
                return {"sets": 4, "reps": "6-8"}
            elif intensity == "expert":
                return {"sets": 4, "reps": "5-7"}
    elif goal == "hypertrophy":
        if category in ["chest", "back", "legs"]:  # Compound movements
            if intensity == "beginner":
                return {"sets": 3, "reps": "10-12"}
            elif intensity == "intermediate":
                return {"sets": 4, "reps": "8-10"}
            elif intensity == "expert":
                return {"sets": 4, "reps": "6-8"}
        else:  # Isolation movements
            if intensity == "beginner":
                return {"sets": 2, "reps": "12-15"}
            elif intensity == "intermediate":
                return {"sets": 3, "reps": "10-12"}
            elif intensity == "expert":
                return {"sets": 3, "reps": "8-10"}
    elif goal == "endurance":
        if intensity == "beginner":
            return {"sets": 2, "reps": "15-20"}
        elif intensity == "intermediate":
            return {"sets": 3, "reps": "12-15"}
        elif intensity == "expert":
            return {"sets": 3, "reps": "12-15"}
    return {"sets": 3, "reps": "10-12"}  # Default fallback

# Generate a Push-Pull-Legs workout plan for a week
workout_plan = {
    "Monday": {
        "Workout": "Push",
        "Exercises": get_random_exercises("chest", "push", "beginner") +
                     get_random_exercises("shoulders", "push", "beginner") +
                     get_random_exercises("triceps", "push", "beginner")
    },
    "Tuesday": {
        "Workout": "Pull",
        "Exercises": get_random_exercises("middle back", "pull", "beginner", 4) +
                     get_random_exercises("biceps", "pull", "beginner")
    },
    "Wednesday": {
        "Workout": "Legs",
        "Exercises": get_random_exercises("quadriceps", "push", "beginner") +
                     get_random_exercises("hamstrings", "pull", "beginner") +
                     get_random_exercises("calves", "push", "beginner")
    },
    "Thursday": {
        "Workout": "Push",
        "Exercises": get_random_exercises("chest", "push", "beginner") +
                     get_random_exercises("shoulders", "push", "beginner") +
                     get_random_exercises("triceps", "push", "beginner")
    },
    "Friday": {
        "Workout": "Pull",
        "Exercises": get_random_exercises("middle back", "pull", "beginner", 4) +
                     get_random_exercises("biceps", "pull", "beginner")
    },
    "Saturday": {
        "Workout": "Legs",
        "Exercises": get_random_exercises("quadriceps", "push", "beginner") +
                     get_random_exercises("hamstrings", "pull", "beginner") +
                     get_random_exercises("calves", "push", "beginner")
    },
    "Sunday": {
        "Workout": "Rest",
        "Exercises": []
    }
}

# Print the workout plan
for day, details in workout_plan.items():
    print(f"{day} ({details['Workout']}):")
    if details['Exercises']:
        for exercise in details['Exercises']:
            # Determine the category dynamically (e.g., chest, shoulders)
            category = "chest" if "chest" in exercise.lower() else \
                       "shoulders" if "shoulder" in exercise.lower() else \
                       "triceps" if "tricep" in exercise.lower() else \
                       "biceps" if "curl" in exercise.lower() or "biceps" in exercise.lower() else \
                       "legs" if "squat" in exercise.lower() or "leg" in exercise.lower() else \
                       "back" if "row" in exercise.lower() or "back" in exercise.lower() else \
                       "calves" if "calf" in exercise.lower() else "general"

            sets_reps = generate_sets_and_reps(category, "beginner", "strength")
            print(f"  - {exercise}")
            print(f"    Sets: {sets_reps['sets']}, Reps: {sets_reps['reps']}")
    else:
        print("  Rest Day")
    print()
