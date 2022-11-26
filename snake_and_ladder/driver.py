from controllers.snake_controller import SnakeController
from controllers.ladder_controller import LadderController
from controllers.player_controller import PlayerController
from controllers.board_controller import BoardController
from controllers.dice_controller import DiceController

snake_controller = SnakeController()
snake_one = snake_controller.add_snake(10, 2)
snake_two = snake_controller.add_snake(99, 12)
snakes = [snake_one,snake_two]

ladder_controller = LadderController()
ladder_one = ladder_controller.add_ladder(5, 25)
ladder_two = ladder_controller.add_ladder(40, 89)
ladders = [ladder_one,ladder_two]

player_controller = PlayerController()
player_one = player_controller.add_player('PLAYER_ONE')
player_two = player_controller.add_player('PLAYER_TWO')
players = [player_one,player_two]

player_positions = {}
player_positions[player_one.name] = 0
player_positions[player_two.name] = 0

dice_controller = DiceController()
dice_obj = dice_controller.add_dice(2)

board_controller = BoardController()
board_controller.add_board(1000)
board_controller.add_snakes(snakes)
board_controller.add_ladders(ladders)
board_controller.add_players(players)
board_controller.add_players_position(player_positions)

board_controller.start_game(dice_obj=dice_obj)