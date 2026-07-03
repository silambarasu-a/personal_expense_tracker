import json

def load_data(file_path = "data/expenses.json"):
    """Load data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_data(data, file_path = "data/expenses.json"):
    """Save data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def append_data(new_data):
    """Append new data to a JSON file."""
    # Load existing data
    data = load_data()

    if not new_data.get("_id"):
        new_data = {"_id": len(data) + 1, **new_data}

    data.append(new_data)

    # Write the updated data back to the file
    save_data(data)

