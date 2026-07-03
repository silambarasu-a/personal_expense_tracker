import uuid
from datetime import datetime

from constants import CATEGORIES, PAYMENT_METHODS
from validators import validate_date_format

from storage import append_data

def add_expense():
    # Function to add an expense
    while True:
        # Get expense details from the user
        # Get the title of the expense
        title = input("Enter the title of the expense: ")
        if not title.strip():
            print("Title cannot be empty. Please try again.")
            continue
        
        # Get the amount of the expense
        try:
            amount = float(input("Enter the amount of the expense: "))
            if amount <= 0:
                print("Amount must be greater than zero. Please try again.")
                continue
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue
        
        # Get the category of the expense
        print("Select the category of the expense: ")
        for index, category in enumerate(CATEGORIES, start=1):
            print(f"{index}. {category}")
        categories_length = len(CATEGORIES)
        try:
            category_choice = int(input(f"Enter your choice (1-{categories_length}): "))
            if 1 <= category_choice <= categories_length:
                category = CATEGORIES[category_choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

        # Get the date of the expense
        expense_date = input("Enter the date of the expense (YYYY-MM-DD): ")
        if not expense_date.strip():
            print("Date cannot be empty. Please try again.")
            continue
        elif not validate_date_format(expense_date):
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue
        
        # Get the payment method of the expense
        print("Select the payment method of the expense: ")
        for index, payemnt_method in enumerate(PAYMENT_METHODS, start=1):
            print(f"{index}. {payemnt_method}")
        payment_methods_length = len(PAYMENT_METHODS)
        try:
            payment_method_choice = int(input(f"Enter your choice (1-{payment_methods_length}): "))
            if 1 <= payment_method_choice <= payment_methods_length:
                payment_method = PAYMENT_METHODS[payment_method_choice - 1]
            else:
                print("Invalid choice of payment method. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

        # Get the notes about the expense which is optional
        notes = (input("Enter any notes about the expense (optional): ")).strip()

        # Create a dictionary to store the expense details
        expense_data = {
            "_id": str(uuid.uuid4()),  # Generate a unique ID for the expense
            "title": title,
            "amount": amount,
            "category": category,
            "date": expense_date,
            "payment_method": payment_method,
            "notes": notes,
            "created_at": str(datetime.now()),  # Store the current date and time as a string
        }

        try:
            # Append the expense data to the JSON file
            append_data(expense_data)
            print("Expense added successfully!")
            break  # Exit the loop after successfully adding the expense
        except Exception as e:
            print(f"An error occurred while adding the expense: {e}")


def view_expenses():
    # Function to view all expenses
    print("Viewing all expenses... (Functionality to be implemented)")

def view_summary():
    # Function to view expense summary
    print("Viewing expense summary... (Functionality to be implemented)")

def set_budget():
    # Function to set monthly budget
    print("Setting monthly budget... (Functionality to be implemented)")