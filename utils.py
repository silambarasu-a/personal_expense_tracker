from datetime import datetime

from constants import CATEGORIES, PAYMENT_METHODS, SEPARATORS
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
        
        case "budget_amount":
            return _prompt("Enter the monthly budget amount: ", validate_amount)

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
        

def filter_expenses(expenses, category=None, start_date=None, end_date=None):
    """Filter expenses based on category and date range."""
    filtered = expenses

    if category:
        filtered = [expense for expense in filtered if expense["category"] == category]

    if start_date:
        filtered = [
            expense
            for expense in filtered
            if datetime.strptime(expense["date"], "%Y-%m-%d") >= start_date
        ]

    if end_date:
        filtered = [
            expense
            for expense in filtered
            if datetime.strptime(expense["date"], "%Y-%m-%d") <= end_date
        ]

    return filtered

def table_print_expenses(expenses):
    """Format expenses for table display."""
   
    print(
            f"{'_id':<5}| {'Title':<20}| {'₹ Amount':<12}| {'Category':<15}| {'Date':<12}| {'Payment Method':<15}| {'Notes':<30}\n"
            f"{SEPARATORS['DASH']}"
        )

        # Print each expense in a formatted manner
    for expense in expenses:
            print(
                f"{expense.get('_id'):<5}| {expense.get('title'):<20}| ₹ {expense.get('amount'):<10,.2f}| {expense.get('category'):<15}| {expense.get('date'):<12}| {expense.get('payment_method'):<15}| {expense.get('notes', 'N/A'):<30}"
            )