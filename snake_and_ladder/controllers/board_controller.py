from services.board_service import BoardService

from controllers.dice_controller import DiceController

class BoardController:
    DEFAULT_BOARD_SIZE = 100
    
    def __init__(self):
        self.board_service = BoardService()

    def add_board(self, size=None):
        if not size:
            size = self.__class__.DEFAULT_BOARD_SIZE
        board_obj = self.board_service.add_board(size)
        return board_obj

    def add_snakes(self, snakes):
        self.board_service.add_snakes(snakes)

    def add_ladders(self, ladders):
        self.board_service.add_ladders(ladders)

    def add_players(self, players):
        self.board_service.add_players(players)

    def add_players_position(self, players_position):
        self.board_service.add_players_position(players_position)
    
    # def add_dice(self, dice_obj):
    #     self.board_service.add_dice(dice_obj)
    
    def start_game(self, dice_obj=None):
        print("Starting the game: ")
        
        board_obj = self.board_service.board
        players_turn = board_obj.players
        ladders =board_obj.ladders
        snakes =board_obj.snakes

        while players_turn:
            current_player = players_turn.pop(0)
            current_player_pos = board_obj.players_position[current_player.name]

            cur_roll = DiceController().roll_dice(dice_obj.id)
            current_player_new_pos = current_player_pos + cur_roll

            if current_player_new_pos == board_obj.size:
                print('{} player reached final position'.format(current_player.name))
                continue
            
            if current_player_new_pos > board_obj.size:
                print('{} : new position is {}'.format(current_player.name, current_player_pos))
                players_turn.append(current_player)
                continue

            matching_ladder = list(filter(lambda x: x.start== current_player_new_pos, ladders))
            matching_snake = list(filter(lambda x: x.start== current_player_new_pos, snakes))
            if matching_ladder:
                current_player_new_pos = matching_ladder[0].end
            elif matching_snake:
                current_player_new_pos = matching_snake[0].end

            board_obj.players_position[current_player.name] = current_player_new_pos
            print('{} : new position is {}'.format(current_player.name, current_player_new_pos))
            players_turn.append(current_player)
