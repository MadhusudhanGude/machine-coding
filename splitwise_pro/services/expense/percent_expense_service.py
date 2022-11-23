from models.percent_expense import PercentExpense
from .expense_service_interface import IExpenseService


class PercentExpenseService(IExpenseService):

    def create_expense(self, id, amount, paid_by, splits, meta_data):
        expense_obj = PercentExpense(id, amount, paid_by, splits, meta_data)
        self.__class__.expenses[expense_obj.id] = expense_obj
        return expense_obj
