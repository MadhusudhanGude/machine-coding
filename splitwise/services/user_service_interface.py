from abc import ABC, abstractmethod


class IUserService(ABC):

    @abstractmethod
    def add_user(self, id, name):
        pass
