
from .interfaces.expense import IExpense
from models.user import User
from .equal_split import EqualSplit


class EqualExpense(IExpense):
    def validate(self):
        for each_split in self.splits:
            if not isinstance(each_split, EqualSplit):
                return False
        return True
