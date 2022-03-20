from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.lives_left = 5
        self.points = 0

    def update_board(self):
        self.clear()
        self.goto(-370, 350)
        self.write(f'Lives left: {self.lives_left}', align='center', font=('Courier', 20, 'normal'))
        self.goto(375, 350)
        self.write(f'Points: {self.points}', align='center', font=('Courier', 20, 'normal'))

    def lose_life(self):
        self.lives_left -= 1
        self.update_board()

    def gain_points(self, points_gained):
        self.points += points_gained
        self.update_board()

    def show_game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER\nYOUR SCORE IS: {self.points}', align='center', font=('Courier', 50, 'normal'))

