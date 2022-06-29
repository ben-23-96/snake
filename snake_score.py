from turtle import Turtle
import os


class Score(Turtle):
    """inherits for the Turtle class, keeps track of the users score, highscore and displays them"""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore_path = os.path.dirname(__file__) + "\\highscore.txt"
        self.hideturtle()

    def add_point(self):
        """adds one to the score attribute of the score object"""
        self.score += 1

    def game_over(self):
        """writes the players score for the previous game as well as the highscore to the board after the player has died"""
        with open(self.highscore_path, 'r') as reader:
            highscore = reader.read()
        self.color('blue')
        self.write(f'Game Over\nScore: {self.score}\nHighscore: {highscore}',
                   font=('comic sans', 20, 'bold'), align='center')

    def new_game(self):
        """resets the score attribute to 0 and clears any writing done the score object from the game"""
        self.score = 0
        self.clear()

    def highscore(self):
        """checks if the current user score is higher than the highscore found in the highscore.txt file,
        if it is rewrites the highscore"""
        with open(self.highscore_path, 'r') as reader:
            score = reader.read()
        if int(score) < self.score:
            with open(self.highscore_path, 'w') as writer:
                writer.write(f"{self.score}")
