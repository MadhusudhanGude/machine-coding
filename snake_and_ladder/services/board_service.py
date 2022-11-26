from models.board import Board


class BoardService:
    board = None

    def add_board(self, size):
        board = Board(size)
        self.__class__.board = board
        return board

    def add_snakes(self, snakes):
        self.__class__.board.snakes = snakes

    def add_ladders(self, ladders):
        self.__class__.board.ladders = ladders

    def add_players(self, players):
        self.__class__.board.players = players


    # def add_dice(self, dice):
    #     self.__class__.board.dice = dice

    def add_players_position(self, players_position):
        self.__class__.board.players_position = players_position
