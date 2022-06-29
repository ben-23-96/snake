from turtle import Turtle


class Board(Turtle):
    """inherits from the Turtle class to draw the walls for the game"""

    def __init__(self):
        super().__init__()

    def new_board(self):
        """sets up the game board creating the yellow walls in which the game is played"""
        self.hideturtle()
        self.penup()
        self.setposition(-355, 295)
        self.pendown()
        self.color('yellow')
        self.pensize(10)
        self.forward(710)
        self.setheading(270)
        self.forward(590)
        self.setheading(180)
        self.forward(710)
        self.setheading(90)
        self.forward(590)
        self.penup()
