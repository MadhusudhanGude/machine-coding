
from .interfaces.split import ISplit


class ExactSplit(ISplit):
    def __init__(self, id, user, amount):
        super().__init__(id, user, amount)
        # super().__init__(id, user)
        # self.__amount = amount

    # @property
    # def amount(self):
    #     return self.__amount
