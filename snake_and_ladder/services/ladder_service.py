from models.ladder import Ladder


class LadderService:
    ladders = {}

    def add_ladder(self, start, end):
        ladder_id = len(self.__class__.ladders) + 1
        ladder = Ladder(ladder_id, start, end)
        self.__class__.ladders[ladder.id] = ladder
        return ladder
