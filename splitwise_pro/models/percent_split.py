from .interfaces.split import ISplit


class PercentSplit(ISplit):
    def __init__(self, id, user, amount, percent):
        super().__init__(id, user, amount)
        self.__percent = percent

    @ property
    def percent(self):
        return self.__percent

    @ percent.setter
    def percent(self, value):
        self.__percent = value
