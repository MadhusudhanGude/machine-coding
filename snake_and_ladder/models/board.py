
class Board:
    def __init__(self, size):
        self.__size = size
        self.__snakes = []
        self.__ladders = []
        self.__players = []
        # self.__dice = None
        self.players_position = {}

    @property
    def size(self):
        return self.__size

    @property
    def dice(self):
        return self.__dice

    @property
    def snakes(self):
        return self.__snakes

    @property
    def players(self):
        return self.__players

    @property
    def ladders(self):
        return self.__ladders

    @property
    def players_position(self):
        return self.__players_position

    @snakes.setter
    def snakes(self, snakes):
        self.__snakes = snakes

    @ladders.setter
    def ladders(self, ladders):
        self.__ladders = ladders

    @dice.setter
    def dice(self, dice):
        self.__dice = dice

    @players.setter
    def players(self, players):
        self.__players = players

    @players_position.setter
    def players_position(self, players_position):
        self.__players_position = players_position
