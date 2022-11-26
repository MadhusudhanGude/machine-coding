from models.player import Player


class PlayerService:
    players = {}

    def add_player(self, name):
        player = Player(name)
        self.__class__.players[player.id] = player
        return player
