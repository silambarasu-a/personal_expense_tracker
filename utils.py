from datetime import datetime

from constants import CATEGORIES, PAYMENT_METHODS
from validators import (
    ValidationError,
    validate_required_text,
    validate_amount,
    validate_choice,
    validate_date,
)


def _prompt(message, validator):
    """Prompt repeatedly until the validator accepts the input, then return the validated value."""
    while True:
        try:
            return validator(input(message))
        except ValidationError as error:
            print(error)


def _print_options(options):
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

def format_expense_date(date_str, format_type="month"):
    """Return the month and year in 'Month YYYY' format from a date string."""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        if format_type == "month":
            return date_obj.month
        else:
            return date_obj
    except ValueError:
        raise ValidationError("Invalid date format. Please use YYYY-MM-DD.")


def get_user_input(type):
    match type:
        case "title":
            return _prompt(
                "Enter the title of the expense: ",
                lambda value: validate_required_text(value, "Title"),
            )

        case "amount":
            return _prompt("Enter the amount of the expense: ", validate_amount)

        case "category":
            print("Select the category of the expense: ")
            _print_options(CATEGORIES)
            return _prompt(
                f"Enter your choice (1-{len(CATEGORIES)}): ",
                lambda value: validate_choice(value, CATEGORIES),
            )

        case "date":
            return _prompt(
                "Enter the date of the expense (YYYY-MM-DD): ",
                validate_date,
            )

        case "payment_method":
            print("Select the payment method of the expense: ")
            _print_options(PAYMENT_METHODS)
            return _prompt(
                f"Enter your choice (1-{len(PAYMENT_METHODS)}): ",
                lambda value: validate_choice(value, PAYMENT_METHODS),
            )

        case "notes":
            notes = input("Enter any notes about the expense (optional): ")
            return notes.strip()  # Notes are optional, so no validation needed
