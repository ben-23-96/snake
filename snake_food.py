from turtle import Turtle
from random import randint


class Food(Turtle):
    """inherits from the Turtle class, creating a turtle object that functions as food in the sanke game"""

    def __init__(self):
        super().__init__()

    def new_food(self):
        """creates a new food block at a random location on the game board"""
        self.penup()
        self.shape('square')
        self.color('blue')
        pos = (randint(-330, 330), randint(-275, 275))
        self.setposition(pos)

    def eaten(self, snake_head):
        """pass in the first item in the snake list, i.e the head, if the head and the food overlap, the food is eaten it returns true"""
        if snake_head.distance(self) < 20:
            self.clear()
            return True
