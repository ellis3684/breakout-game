import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        starting_speed = 0.02
        # Speed levels go from 1 to 5, for starting-easy-medium-hard-top.
        self.speed_level = 1
        self.ball_speed = starting_speed
        self.easy_speed = starting_speed * 0.9
        self.medium_speed = starting_speed * 0.8
        self.hard_speed = starting_speed * 0.7
        self.top_speed = starting_speed * 0.6

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.x_move = random.choice([10, -10])
        self.y_move = 10