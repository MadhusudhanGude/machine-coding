from models.equal_expense import EqualExpense
from .expense_service_interface import IExpenseService


class EqualExpenseService(IExpenseService):

    def create_expense(self, id, amount, paid_by, splits, meta_data):
        expense_obj = EqualExpense(id, amount, paid_by, splits, meta_data)
        self.__class__.expenses[expense_obj.id] = expense_obj
        return expense_obj
