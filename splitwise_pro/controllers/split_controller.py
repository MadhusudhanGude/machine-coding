
class SplitController:
    def __init__(self, split_service):
        self.split_service = split_service

    def add_split(self, user, amount=None, percent=None, total_amount=None):
        new_id = 'split' + \
            str(len(self.split_service.splits) + 1)
        split_obj = self.split_service.create_split(
            new_id, user, amount=amount, percent=percent, total_amount=total_amount)
        return split_obj
