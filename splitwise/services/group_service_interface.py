from abc import ABC, abstractmethod


class IGroupService(ABC):

    @abstractmethod
    def add_group(self, id, name, members):
        pass
