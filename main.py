from turtle import Screen, Turtle, done
from snake_body import Snake
from snake_food import Food
from snake_score import Score
from snake_board import Board
import time

screen = Screen()
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

score = Score()
board = Board()
board.new_board()
food = Food()
food.new_food()

snake = []
x = 0
for _ in range(3):
    block = Snake()
    snake.append(block)
    block.create_block((x, 0))
    x -= 20

difficulties = {'easy': 0.2, 'medium': 0.1, 'hard': 0.05}
difficulty = screen.textinput(
    "Difficulty", "Type easy/medium/hard for new game:  ")

screen.onkeypress(snake[0].turn_up, 'Up')
screen.onkeypress(snake[0].turn_down, 'Down')
screen.onkeypress(snake[0].turn_right, 'Right')
screen.onkeypress(snake[0].turn_left, 'Left')

game_finished = False

while not game_finished:
    screen.update()
    screen.listen()

    snake_tail = snake[-1].snake_tail()
    snake[0].move_forward(snake)

    if food.eaten(snake[0]):
        food.new_food()
        score.add_point()
        new_tail = Snake()
        snake.append(new_tail)
        new_tail.create_block(snake_tail)

    if snake[0].body_collison(snake) or snake[0].wall_collison():
        score.highscore()
        score.game_over()
        new_game = screen.textinput(
            "New Game", "Type yes or no for new game:  ")
        if new_game == 'yes':
            difficulty = screen.textinput(
                "Difficulty", "Type easy/medium/hard for new game:  ")
            snake = snake[0].new_game(snake)
            food.new_food()
            score.new_game()
        else:
            game_finished = True

    time.sleep(difficulties[difficulty])


done()
