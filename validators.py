from datetime import datetime


def validate_date_format(date_string):
    # Function to validate the date format (YYYY-MM-DD)
    try:
        value = datetime.strptime(date_string, "%Y-%m-%d")
        print(f"Validated date: {value}")  # Debugging statement to show the parsed date
        return True
    except ValueError:
        return False