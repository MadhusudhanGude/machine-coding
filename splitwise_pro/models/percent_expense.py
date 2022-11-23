
from .interfaces.expense import IExpense


class PercentExpense(IExpense):

    def validate(self):
        percent_sum_total = 0
        from .percent_split import PercentSplit
        for each_split in self.splits:

            if not isinstance(each_split, PercentSplit):
                return False
            percent_sum_total += each_split.percent

        if percent_sum_total != 100:
            return False

        return True
