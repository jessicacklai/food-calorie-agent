# Food & Calorie Agent

A mini self‑agent project for practising the workflow of an LLM agent. The agent helps you record the food and drink you consume each day, along with their calories, for every meal. It also calculates the total sum of calories consumed.

## Features
- Record meals (breakfast, lunch, dinner, snacks) with item names and calorie counts.
- Calculate the total sum of calories for the day.

## How to Use
1. Run the script (command depends on your implementation).
2. Enter the meal type, food/drink name, and calories.
3. Request the total calories for the day.

## Data Format

The agent stores your daily food records in JSON format. Example:

```json
{
  "2026-03-22": [
    {
      "meal_name": "Breakfast",
      "food_name": "2 eggs",
      "calories": 140
    },
    {
      "meal_name": "Breakfast",
      "food_name": "celery",
      "calories": 70
    },
    {
      "meal_name": "breakfast",
      "food_name": "2 slices of bread",
      "calories": 250
    },
    {
      "meal_name": "dinner",
      "food_name": "50g pasta",
      "calories": 180
    },
    {
      "meal_name": "dinner",
      "food_name": "vegetables",
      "calories": 100
    },
    {
      "meal_name": "dinner",
      "food_name": "fish",
      "calories": 100
    }
  ]
}
