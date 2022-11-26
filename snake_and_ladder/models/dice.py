import uuid

class Dice:
    def __init__(self, number_of_dice):
        self.__id = uuid.uuid4().hex
        self.__number_of_dice = number_of_dice

    @property
    def number_of_dice(self):
        return self.__number_of_dice

    @property
    def id(self):
        return self.__id
