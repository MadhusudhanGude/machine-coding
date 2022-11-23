from models.user import User
from abc import ABC, abstractmethod


class IExpense(ABC):
    def __init__(self, id: int, amount: float, paid_by: User, splits, meta_data):
        self.__id = id
        self.__amount = amount
        self.__paid_by = paid_by
        self.__splits = splits
        self.__meta_data = meta_data

        if not self.validate():
            raise Exception

    @abstractmethod
    def validate(self):
        pass

    @property
    def id(self):
        return self.__id

    @property
    def paid_by(self):
        return self.__paid_by

    @paid_by.setter
    def paid_by(self, value):
        self.__paid_by = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def splits(self):
        return self.__splits

    @splits.setter
    def splits(self, value):
        self.__splits = value

    @property
    def meta_data(self):
        return self.__meta_data

    @meta_data.setter
    def meta_data(self, value):
        self.__meta_data = value
