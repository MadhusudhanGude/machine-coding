from models.exact_expense import ExactExpense

from .expense_service_interface import IExpenseService


class ExactExpenseService(IExpenseService):

    def create_expense(self, id, amount, paid_by, splits, meta_data):
        expense_obj = ExactExpense(id, amount, paid_by, splits, meta_data)
        self.__class__.expenses[expense_obj.id] = expense_obj
        return expense_obj
