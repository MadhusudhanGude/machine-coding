from .split_service_interface import ISplitService
from models.equal_split import EqualSplit


class EqualSplitService(ISplitService):

    def create_split(self, id, user, amount=0,  *args, **kwargs):
        split_obj = EqualSplit(id, user, amount)
        self.__class__.splits[split_obj.id] = split_obj
        return split_obj
