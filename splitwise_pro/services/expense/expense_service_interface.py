from abc import ABC, abstractmethod


class IExpenseService(ABC):
    expenses = {}

    @abstractmethod
    def create_expense(self, id,  expense_type, amount, paid_by, splits, meta_data):
        pass
