from turtle import Turtle


class Bar(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('green')
        self.shapesize(stretch_len=8, stretch_wid=1)
        self.penup()
        self.goto(0, -300)
        self.move = 20
    
    def move_left(self):
        new_x = self.xcor() - self.move
        self.goto(new_x, self.ycor())
    
    def move_right(self):
        new_x = self.xcor() + self.move
        self.goto(new_x, self.ycor())
