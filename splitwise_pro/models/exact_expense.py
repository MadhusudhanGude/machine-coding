
from .interfaces.expense import IExpense


class ExactExpense(IExpense):

    def validate(self):
        sum_split_amount = 0
        from .exact_split import ExactSplit
        for each_split in self.splits:
            if not isinstance(each_split, ExactSplit):
                return False

            sum_split_amount += each_split.amount

        if sum_split_amount != self.amount:
            return False

        return True
