from abc import ABC, abstractmethod


class ISplitService(ABC):
    splits = {}

    @abstractmethod
    def create_split(self, *args, **kwargs):
        pass
