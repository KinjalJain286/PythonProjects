import json
from pathlib import Path
from typing import List
from .expense import Expense

class ExpenseStorage:
    def __init__(self, file_path: str = "expenses.json"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def save_expenses(self, expenses: List[Expense]) -> None:
        data = [expense.to_dict() for expense in expenses]
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=2)

    def load_expenses(self) -> List[Expense]:
        if not self.file_path.exists():
            return []
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            return [Expense.from_dict(item) for item in data]
        except json.JSONDecodeError:
            return []
