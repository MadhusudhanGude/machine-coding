from models.snake import Snake


class SnakeService:
    snakes = {}

    def add_snake(self, start, end):
        snake_id = len(self.__class__.snakes) + 1
        snake = Snake(snake_id, start, end)
        self.__class__.snakes[snake.id] = snake
        return snake
