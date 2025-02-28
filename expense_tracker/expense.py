from datetime import datetime
from decimal import Decimal
from typing import Optional

class Expense:
    def __init__(self, amount: Decimal, description: str, category: str, date: Optional[datetime] = None):
        self.amount = amount
        self.description = description
        self.category = category
        self.date = date or datetime.now()

    def to_dict(self):
        return {
            'amount': str(self.amount),
            'description': self.description,
            'category': self.category,
            'date': self.date.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            amount=Decimal(data['amount']),
            description=data['description'],
            category=data['category'],
            date=datetime.fromisoformat(data['date'])
        )
