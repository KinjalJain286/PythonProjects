from .storage import ExpenseStorage
from .interface import ExpenseUI
from .analysis import ExpenseAnalyzer

def main():
    storage = ExpenseStorage()
    expenses = storage.load_expenses()

    while True:
        print("\n1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        
        choice = input("Select an option: ")

        if choice == "1":
            expense = ExpenseUI.get_expense_input()
            if expense:
                expenses.append(expense)
                storage.save_expenses(expenses)
                print("Expense added successfully!")

        elif choice == "2":
            analyzer = ExpenseAnalyzer()
            monthly_summary = analyzer.monthly_summary(expenses)
            category_summary = analyzer.category_summary(expenses)
            ExpenseUI.display_summary(monthly_summary, category_summary)

        elif choice == "3":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
