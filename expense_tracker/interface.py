from decimal import Decimal, InvalidOperation
from typing import List, Optional
from .expense import Expense

class ExpenseUI:
    CATEGORIES = ['food', 'transportation', 'entertainment', 'utilities', 'other']

    @staticmethod
    def get_expense_input() -> Optional[Expense]:
        try:
            print("\nEnter expense details:")
            amount = Decimal(input("Amount: "))
            description = input("Description: ")
            
            print("\nAvailable categories:")
            for i, category in enumerate(ExpenseUI.CATEGORIES, 1):
                print(f"{i}. {category}")
            category_idx = int(input("Select category number: ")) - 1
            category = ExpenseUI.CATEGORIES[category_idx]

            return Expense(amount, description, category)
        except (InvalidOperation, ValueError, IndexError):
            print("Invalid input. Please try again.")
            return None

    @staticmethod
    def display_summary(monthly_summary: dict, category_summary: dict):
        print("\n=== Monthly Summary ===")
        for month, total in monthly_summary.items():
            print(f"{month}: ${total:.2f}")

        print("\n=== Category Summary ===")
        for category, total in category_summary.items():
            print(f"{category}: ${total:.2f}")
