from services.player_service import PlayerService


class PlayerController:
    def __init__(self):
        self.player_service = PlayerService()

    def add_player(self, name):
        player_obj = self.player_service.add_player(name)
        return player_obj
