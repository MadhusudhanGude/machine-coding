from .split_service_interface import ISplitService
from models.exact_split import ExactSplit


class ExactSplitService(ISplitService):

    def create_split(self, id, user, amount=0, *args, **kwargs):
        split_obj = ExactSplit(id, user, amount)
        self.__class__.splits[split_obj.id] = split_obj
        return split_obj
