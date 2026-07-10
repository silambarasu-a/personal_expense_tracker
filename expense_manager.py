from datetime import datetime, timedelta

from constants import SEPARATORS
from utils import filter_expenses, format_expense_date, get_user_input, table_print_expenses
from storage import append_data, load_data, save_data
       

def get_overiew():
    # Function to get an overview of expenses
    expenses = load_data() or []
    budget = (load_data("data/settings.json") or {}).get("monthly_budget", 0)

    # Calculate the start and end dates for the current month
    current_month_start_date = datetime(datetime.now().year, datetime.now().month, 1)
    current_month_end_date = datetime(datetime.now().year, datetime.now().month + 1, 1) - timedelta(days=1)

    current_month_expenses = filter_expenses(expenses, start_date=current_month_start_date, end_date=current_month_end_date)

    available_budget = budget - sum(expense.get("amount", 0) for expense in current_month_expenses)

    return { "available_budget": available_budget, "current_month_expenses": current_month_expenses, "budget": budget }


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

    if data is None:
        data = []

    print(SEPARATORS["EQUALS"])

    # Check if there are any expenses to display
    if len(data) == 0:
        print("No expenses found.")
    else:
        # Print the header for the expense table
        table_print_expenses(data)

    print(SEPARATORS["EQUALS"])

def view_summary():
    # Function to view expense summary
    # Load the expense data
    data = load_data()

    if data is None:
        data = []

    total_expenses = 0

    categories = {}
    payment_methods = {}

    current_month_expenses = 0
    current_month_records = 0

    current_month_max_expense = None
    current_month_min_expense = None

    if data:
        for expense in data:
            
            #overall calculation
            total_expenses += expense.get("amount", 0)

            # Categorize expenses
            category = expense.get("category", "Uncategorized")
            if category not in categories:
                categories[category] = 0
            categories[category] += expense.get("amount", 0)

            # Payment method calculation
            payment_method = expense.get("payment_method", "Unknown")
            if payment_method not in payment_methods:
                payment_methods[payment_method] = 0
            payment_methods[payment_method] += expense.get("amount", 0)

            #current month calculation
            if format_expense_date(expense.get("date"), "month") == datetime.now().month:
                current_month_records += 1
                current_month_expenses += expense.get("amount", 0)
                if current_month_max_expense is None or expense.get("amount", 0) > current_month_max_expense.get("amount", 0):
                    current_month_max_expense = expense
                if current_month_min_expense is None or expense.get("amount", 0) < current_month_min_expense.get("amount", 0):
                    current_month_min_expense = expense

    # Display the summary
    print(SEPARATORS["EQUALS"])
    print("Expense Summary:")

    print(f"Total Expenses: ₹ {total_expenses:,.2f}")
    print(f"Current Month Expenses: ₹ {current_month_expenses:,.2f} (Records: {current_month_records})")

    if current_month_max_expense:
        print(f"\nHighest Expense This Month: ₹ {current_month_max_expense.get('amount', 0):,.2f} - {current_month_max_expense.get('title', 'N/A')} on {current_month_max_expense.get('date', 'N/A')}")

    if current_month_min_expense:
        print(f"Lowest Expense This Month: ₹ {current_month_min_expense.get('amount', 0):,.2f} - {current_month_min_expense.get('title', 'N/A')} on {current_month_min_expense.get('date', 'N/A')}")

    print("\nExpenses by Category:")
    for category, amount in categories.items():
        if amount > 0:
          print(f"{category}: ₹ {amount:,.2f}")
    
    print("\nExpenses by Payment Method:")
    for method, amount in payment_methods.items():
        if amount > 0:
          print(f"{method}: ₹ {amount:,.2f}")
    
    print(SEPARATORS["EQUALS"])


def set_budget():
    # Function to set monthly budget
    while True:
        # Get budget amount from the user
        budget_amount = get_user_input("budget_amount")

        # Load existing data to check if budget already exists
        data = load_data("data/settings.json")

        if data is None:
            data = {}
        
        # Update the budget amount in the settings
        data["monthly_budget"] = budget_amount
        saved = save_data(data, "data/settings.json")

        if saved:
            print(f"Monthly budget set to ₹ {budget_amount:,.2f}")
            break  # Exit the loop after successfully setting the budget
        else:
            print("An error occurred while setting the budget. Please try again.")


def edit_expense():
    '''Function to edit an existing expense'''

    while True:

        print(SEPARATORS["EQUALS"])

        expenses = []

        id_to_edit = input("Enter the ID of the expense you want to edit (or type 'exit' to go back): ").strip()

        if id_to_edit.lower() == 'exit':
            break

        # Load the expense data
        expenses = load_data("data/expenses.json") or expenses

        # Find the expense with the given ID
        expense_index = next((index for index, expense in enumerate(expenses) if str(expense.get("_id")) == id_to_edit), None)

        if expense_index is None:
            print(f"No expense found with ID {id_to_edit}. Please try again.")
            continue
        else:
            expense_to_edit = expenses[expense_index]

            print(SEPARATORS["DASH"])
            table_print_expenses([expense_to_edit])
            print(SEPARATORS["EQUALS"])

            # Prompt the user for getting key they want to edit and the new value for that key
            key_to_edit = input("Enter the field you want to edit (title, amount, category, date, payment_method, notes) or type 'exit' to go back: ").strip()

            if key_to_edit.lower() == 'exit':
                break
            elif key_to_edit not in expense_to_edit:
                print(f"Invalid field '{key_to_edit}'. Please try again.")
                continue
            else:
                new_value = get_user_input(key_to_edit)

                # Update the expense with the new value
                expense_to_edit[key_to_edit] = new_value

                # Save the updated expenses back to the JSON file
                expenses[expense_index] = expense_to_edit
                saved = save_data(expenses, "data/expenses.json")

                if saved:
                    print(f"Expense with ID {id_to_edit} has been updated successfully.")

                    print(SEPARATORS["DASH"])
                    table_print_expenses([expense_to_edit])
                    print(SEPARATORS["DASH"])

                    break  # Exit the loop after successfully editing the expense
                else:
                    print("An error occurred while updating the expense. Please try again.")

            

def search_expenses():
    '''Function to search expenses based on various criteria'''

    while True:

        print(SEPARATORS["EQUALS"])

        keywords = input("Enter keywords to search for (or type 'exit' to go back): ").strip()

        if keywords.lower() == 'exit':
            break

        # Perform the search based on keywords
        expenses = load_data("data/expenses.json") or []
        results = [
                expense 
                for expense in expenses 
                if any(
                    keyword.lower() in str(value).lower() 
                    for keyword in keywords.split() 
                    for value in expense.values()
                )
            ]

        if results:
            print(f"Search results for '{keywords}':")

            print(SEPARATORS["DASH"])

            table_print_expenses(results)

        else:
            print(f"No expenses found for '{keywords}'.")
        

