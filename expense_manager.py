from uuid import uuid4
from datetime import datetime

from utils import get_user_input
from storage import append_data, load_data
       

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

    # Load the expense data from the JSON file
    data = load_data()

    print(f"{'=' * 140}")

    # Check if there are any expenses to display
    if len(data) == 0:
        print("No expenses found.")
    else:
        # Print the header for the expense table
        print(
            f"{'_id':<5}| {'Title':<20}| {'₹ Amount':<12}| {'Category':<15}| {'Date':<12}| {'Payment Method':<15}| {'Notes':<30}\n"
            f"{'-' * 140}"
        )

        # Print each expense in a formatted manner
        for expense in data:
            print(
                f"{expense.get('_id'):<5}| {expense.get('title'):<20}| ₹ {expense.get('amount'):<10,.2f}| {expense.get('category'):<15}| {expense.get('date'):<12}| {expense.get('payment_method'):<15}| {expense.get('notes', 'N/A'):<30}"
            )

    print(f"{'=' * 140}")

def view_summary():
    # Function to view expense summary
    print("Viewing expense summary... (Functionality to be implemented)")

def set_budget():
    # Function to set monthly budget
    print("Setting monthly budget... (Functionality to be implemented)")