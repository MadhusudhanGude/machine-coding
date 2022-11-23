from ..user import User
from abc import ABC


class ISplit(ABC):
    def __init__(self, id: int, user: User, amount: float):
        self.__id = id
        self.__user = user
        self.__amount = amount

    @property
    def id(self):
        return self.__id

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, value):
        self.__user = value

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value
