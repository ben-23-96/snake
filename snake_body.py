from turtle import Turtle


class Snake(Turtle):
    """inherits from the Turtle class, creates a turtle object with added methods to be used to function as a snake in game as an list of snake objects"""

    def __init__(self) -> None:
        super().__init__()

    def create_block(self, pos):
        """"creates one turtle object, at the position pos to be given as (x, y) tuple, that is a square to make up one block of the snake as it moves"""
        self.penup()
        self.shape('square')
        self.color('white')
        self.setposition(pos)

    def move_forward(self, snake):
        """call on the first snake object in a list of snake objects that make up the snake to move the snake, pass in also the list of snake objects"""
        for i in range((len(snake)-1), 0, -1):
            if i == 0:
                continue
            pos = snake[i-1].position()
            snake[i].setposition(pos)

        snake[0].forward(20)

    def snake_tail(self):
        """call on the last snake object in the snake array to return its co-ordinates, use these co-ordinates when adding new blocks to the end of the snake"""
        tail_coordinates = (round(self.xcor()), round(self.ycor()))
        return tail_coordinates

    def body_collison(self, snake):
        """"call on any object in snake and pass in the snake array,
        returns true if the snake has collided with itself by checking for duplicates of the position on screen of each object in the snake array"""
        snake_set = set()
        for block in snake:
            x = block.xcor()
            y = block.ycor()
            pos = (round(x), round(y))
            if pos in snake_set:
                return True
            else:
                snake_set.add(pos)
        return False

    def wall_collison(self):
        """call on the first snake object in the snake array, returns true if the snake collides with the wall"""
        if self.xcor() >= 350 or self.xcor() <= -350 or self.ycor() <= -300 or self.ycor() >= 300:
            return True

    def new_game(self, snake):
        """call when starting a new game, clears all snake objects that have been gained in previous game, 
        moves the intial 3 snake objects back to center and returns the snake list with just the 3 intial snake objects"""
        for block in snake[3:]:
            block.clear()
            block.hideturtle()

        x = 0
        for block in snake[:3]:
            block.setposition((x, 0))
            block.setheading(0)
            x -= 20

        return snake[:3]

    def turn_up(self):
        """sets the snake direction north"""
        if self.heading() != 270:
            self.setheading(90)

    def turn_down(self):
        """sets the snake direction south"""
        if self.heading() != 90:
            self.setheading(270)

    def turn_right(self):
        """sets the snake direction east"""
        if self.heading() != 180:
            self.setheading(0)

    def turn_left(self):
        """"sets the snake direction west"""
        if self.heading() != 0:
            self.setheading(180)
