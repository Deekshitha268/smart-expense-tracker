import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data.json")


def load_expenses():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)