from .bill_service_interface import IBillService
from models.bill import Bill
from abc import ABC, abstractmethod


class BillService(IBillService):
    bills = {}

    def add_bill(self, id, name, amount, contributions, paid_by):
        bill = Bill(id, name, amount, contributions, paid_by)
        self.__class__.bills[id] = bill
        return bill
