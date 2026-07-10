import json

def load_data(file_path = "data/expenses.json"):
    """Load data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def save_data(data, file_path = "data/expenses.json"):
    """Save data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            return True
    except Exception as e:
        print(f"An error occurred while saving data: {e}")
        return False

def append_data(new_data):
    """Append new data to a JSON file."""
    # Load existing data
    data = load_data()

    if data is None:
        data = []

    if not new_data.get("_id"):
        new_data = {"_id": len(data) + 1, **new_data}

    data.append(new_data)

    # Write the updated data back to the file
    save_data(data)

