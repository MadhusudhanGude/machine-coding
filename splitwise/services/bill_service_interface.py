from abc import ABC, abstractmethod


class IBillService(ABC):

    @abstractmethod
    def add_bill(self, id, name, amount, contributions, paid_by):
        pass
