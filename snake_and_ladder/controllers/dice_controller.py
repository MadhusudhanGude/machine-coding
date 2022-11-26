from services.dice_service import DiceService
from random import randint

class DiceController:
    def __init__(self):
        self.dice_service = DiceService()

    def add_dice(self, num_of_dice):
        dice_obj = self.dice_service.add_dice(num_of_dice)
        return dice_obj

    def roll_dice(self, dice_id):
        dice_obj = self.dice_service.dice.get(dice_id)
        return randint(1 * dice_obj.number_of_dice, 6 * dice_obj.number_of_dice)
