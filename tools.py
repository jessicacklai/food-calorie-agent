import json
from datetime import date
from pathlib import Path
import os

base_dir = Path("./test")
today = str(date.today())

def load_json_safe(path):
    try:
        with open(path, "r") as f:
            content = f.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except:
        return {}

def log_food(meal_name: str, food_name: str, calories: int) -> str:
    """Log a food and/or drink item with its calorie count for a given meal."""
    
    base_dir.mkdir(exist_ok=True)
    log_path = base_dir / f"{today}_diet_log.json"

    log = load_json_safe(log_path)

    if today not in log:
        log[today] = []

    log[today].append({
        "meal_name": meal_name,
        "food_name": food_name,
        "calories": calories
    })

    with open(log_path, "w") as f:
        json.dump(log, f, indent=2)

    return f"Recorded {food_name} ({calories} kcals) for {meal_name}."



def get_todays_calories() -> str:
    """Return total calories consumed today."""
    log_path = base_dir / f"{today}_diet_log.json"
    if not log_path.exists():
        return "No data for today."

    with open(log_path, "r") as f:
        log = json.load(f)

    total = sum(item["calories"] for item in log.get(today, []))
    return f"The total calories consumed today is '{total}'"