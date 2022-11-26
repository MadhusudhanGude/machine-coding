import uuid


class Player:
    def __init__(self, name):
        self.__id = uuid.uuid4().hex
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
