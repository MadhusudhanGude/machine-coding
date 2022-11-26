from services.ladder_service import LadderService


class LadderController:
    def __init__(self):
        self.ladder_service = LadderService()

    def add_ladder(self, start, end):
        # new_id = 'ladder' + \
        #     str(len(self.ladder_service.ladders) + 1)
        ladder_obj = self.ladder_service.add_ladder(start, end)
        return ladder_obj
