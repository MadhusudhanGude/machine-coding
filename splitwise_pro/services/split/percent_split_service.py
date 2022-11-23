from .split_service_interface import ISplitService
from models.percent_split import PercentSplit


class PercentSplitService(ISplitService):

    def create_split(self, id, user, percent=0, total_amount=0, *args, **kwargs):
        amount = total_amount * percent/100
        split_obj = PercentSplit(id, user, amount, percent)
        self.__class__.splits[split_obj.id] = split_obj
        return split_obj
