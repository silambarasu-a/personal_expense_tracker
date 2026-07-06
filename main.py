from expense_manager import add_expense, view_expenses, view_summary, set_budget
from constants import SEPARATORS

def show_menu():
    print("\n" + SEPARATORS["EQUALS"])
    print("-----------------------Hello! Welcome to the Personal Expense Tracker-----------------------")
    print("This is a simple program that helps you track your personal expenses.")
    print("You can add, view, and delete expenses at any time.")
    print(SEPARATORS["EQUALS"])
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Expense Summary")
    print("4. Set Monthly Budget")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            set_budget()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()







