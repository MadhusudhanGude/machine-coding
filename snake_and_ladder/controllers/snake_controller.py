from services.snake_service import SnakeService


class SnakeController:
    def __init__(self):
        self.snake_service = SnakeService()
        
    def add_snake(self, start, end):
        # new_id = 'snake' + \
        #     str(len(self.snake_service.snakes) + 1)
        snake_obj = self.snake_service.add_snake(start, end)
        return snake_obj
