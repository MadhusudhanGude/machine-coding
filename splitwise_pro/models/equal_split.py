from .interfaces.split import ISplit


class EqualSplit(ISplit):
    def __init__(self, id, user, amount):
        super().__init__(id, user, amount)
