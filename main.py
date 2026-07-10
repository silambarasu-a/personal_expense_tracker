from expense_manager import add_expense, get_overiew, search_expenses, view_expenses, view_summary, set_budget
from constants import SEPARATORS

MENU = [
    ("Add Expense", add_expense), 
    ("View All Expenses", view_expenses), 
    ("View Expense Summary", view_summary), 
    ("Set Monthly Budget", set_budget), 
    ("Edit an Expense", None), 
    ("Search Expenses", search_expenses), 
    ("Exit", 0)
]

def show_menu():


    print("\n" + SEPARATORS["EQUALS"])
    print("-----------------------Hello! Welcome to the Personal Expense Tracker-----------------------")
    print("This is a simple program that helps you track your personal expenses.")
    print("You can add, view, and delete expenses at any time.")
    
    print(SEPARATORS["EQUALS"])

    overview = get_overiew()
    budget_amount = overview.get('budget', 0)
    available_budget = overview.get('available_budget', 0)

    print(f"Monthly Budget: ₹ {budget_amount:,.2f}")
    print(available_budget >= 0 and f"Current Month Available Budget: ₹ {available_budget:,.2f}" or  f"Over Budget by: ₹ {abs(available_budget):,.2f}")
    
    print(SEPARATORS["EQUALS"])

    for i, option in enumerate(MENU, start=1):
        print(f"{i}. {option[0]}")


def main():
    while True:
        show_menu()
        choice = input(f"Enter your choice ({1}-{len(MENU)}): ")

        try:
            choice = int(choice)
            if choice < 1 or choice > len(MENU):
                print("Invalid choice. Please try again.")
                continue
            else:
                menu_item = MENU[choice - 1][1]
                if menu_item is None:
                    print("This feature is not yet implemented. Please choose another option.")
                    continue
                else:
                    if menu_item == 0:
                        print("Exiting the program. Goodbye!")
                        break
                    else:
                        menu_item()
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue


if __name__ == "__main__":
    main()







