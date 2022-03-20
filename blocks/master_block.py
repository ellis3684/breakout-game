from turtle import Turtle


class MasterBlock(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=0.7)
        self.penup()
        self.list_of_blocks = []
        self.list_of_easy_blocks = []
        self.list_of_medium_blocks = []
        self.list_of_hard_blocks = []
        self.list_of_top_blocks = []

    def break_on_contact(self):
        self.hideturtle()

    def reset_blocks(self):
        self.list_of_blocks = []
        self.list_of_easy_blocks = []
        self.list_of_medium_blocks = []
        self.list_of_hard_blocks = []
        self.list_of_top_blocks = []
