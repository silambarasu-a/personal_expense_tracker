from uuid import uuid4
from datetime import datetime

from utils import get_user_input
from storage import append_data
       

def add_expense():
    # Function to add an expense
    while True:
        # Get expense details from the user
        # Get the title of the expense
        title = get_user_input("title")
        
        # Get the amount of the expense
        amount = get_user_input("amount")
        
        # Get the category of the expense
        category = get_user_input("category")
        
        # Get the date of the expense
        expense_date = get_user_input("date")
        
        # Get the payment method of the expense
        payment_method = get_user_input("payment_method")

        # Get the notes about the expense which is optional
        notes = get_user_input("notes")

        # Create a dictionary to store the expense details
        expense_data = {
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