from models.dice import Dice


class DiceService:
    dice = {}

    def add_dice(self, num_of_dice):
        dice_obj = Dice(num_of_dice)
        self.__class__.dice[dice_obj.id] = dice_obj
        return dice_obj
