from typing import List
from collections import defaultdict
from decimal import Decimal
from datetime import datetime
from .expense import Expense

class ExpenseAnalyzer:
    @staticmethod
    def monthly_summary(expenses: List[Expense]) -> dict:
        monthly_totals = defaultdict(Decimal)
        for expense in expenses:
            month_key = expense.date.strftime("%Y-%m")
            monthly_totals[month_key] += expense.amount
        return dict(monthly_totals)

    @staticmethod
    def category_summary(expenses: List[Expense]) -> dict:
        category_totals = defaultdict(Decimal)
        for expense in expenses:
            category_totals[expense.category] += expense.amount
        return dict(category_totals)
