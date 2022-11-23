
class BillController:
    def __init__(self, bill_service) -> None:
        self.bill_service = bill_service

    def add_bill(self, id, name, amount, contributions, paid_by):
        self.bill_service.add_bill(id, name, amount, contributions, paid_by)

    def get_user_balance(self, user_id):
        balance = 0
        for bill_id in self.bill_service.bills:
            bill = self.bill_service.bills.get(bill_id)
            if user_id in bill.contributions:
                balance = balance - bill.contributions.get(user_id)
            if user_id in bill.paid_by:
                balance = balance + bill.paid_by.get(user_id)

        return balance
