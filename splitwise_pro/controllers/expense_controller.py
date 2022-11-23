from services.expense.expense_service_interface import IExpenseService


class ExpenseController:
    def __init__(self, expense_service=None):
        self.expense_service = expense_service

    def add_expense(self, amount, paid_by, splits, meta_data):
        new_id = 'expense' + \
            str(len(self.expense_service.expenses) + 1)
        expense_obj = self.expense_service.create_expense(
            new_id, amount, paid_by, splits, meta_data)
        return expense_obj

    @classmethod
    def get_user_balance_amount(cls, user_id):
        balance = 0

        for expense_id in IExpenseService.expenses:
            expense = IExpenseService.expenses.get(expense_id)
            paid_by = expense.paid_by
            if paid_by == user_id:
                balance += expense.amount

            for each_split in expense.splits:
                if each_split.user.id == user_id:
                    balance -= each_split.amount

        return balance

    @classmethod
    def get_user_balance(cls, user_id, lending_enabed=True):
        balances = {}
        for expense_id in IExpenseService.expenses:
            expense = IExpenseService.expenses.get(expense_id)
            paid_by = expense.paid_by
            for each_split in expense.splits:
                if paid_by == user_id and each_split.user.id != user_id:
                    if each_split.user.id not in balances:
                        balances[each_split.user.id] = 0
                    balances[each_split.user.id] += each_split.amount

                elif paid_by != user_id and each_split.user.id == user_id:
                    if paid_by not in balances:
                        balances[paid_by] = 0
                    balances[paid_by] -= each_split.amount

        print('------ {} BALANCES -------'.format(user_id))
        if not balances:
            print('No balances')
        else:
            for other_person, amount in balances.items():
                if amount > 0 and lending_enabed:
                    print('{} owes {}: {}'.format(
                        other_person, user_id, abs(amount)))
                elif amount < 0:
                    print('{} owes {}: {}'.format(
                        user_id, other_person, abs(amount)))
