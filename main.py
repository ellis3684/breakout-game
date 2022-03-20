from turtle import Screen
from bar import Bar
from ball import Ball
from blocks.master_block import MasterBlock
from scoreboard import Scoreboard
from blocks import easy_block, medium_block, hard_block, top_block
import time

# Screen set up
screen = Screen()
screen.bgcolor('black')
screen.setup(width=960, height=760)
screen.title('Breakout - by Corey Ellis')
screen.tracer(0)

# User bar and ball class instances
bar = Bar()
ball = Ball()
scoreboard = Scoreboard()
master_block = MasterBlock()
master_block.hideturtle()


# Set starting blocks
def set_starting_blocks():
    """Sets blocks according to color, and keeps track of each color's blocks."""
    for x in range(-454, 447, 50):
        new_block = easy_block.EasyBlock()
        new_block.goto(x, 150)
        master_block.list_of_blocks.append(new_block)
        master_block.list_of_easy_blocks.append(new_block)
        new_block = easy_block.EasyBlock()
        new_block.goto(x, 175)
        master_block.list_of_blocks.append(new_block)
        master_block.list_of_easy_blocks.append(new_block)

        new_block = medium_block.MediumBlock()
        new_block.goto(x, 200)
        master_block.list_of_blocks.append(new_block)
        master_block.list_of_medium_blocks.append(new_block)
        new_block = medium_block.MediumBlock()
        new_block.goto(x, 225)
        master_block.list_of_blocks.append(new_block)
        master_block.list_of_medium_blocks.append(new_block)

        new_block = hard_block.HardBlock()
        new_block.goto(x, 250)
        master_block.list_of_blocks.append(new_block)
        master_block.list_of_hard_blocks.append(new_block)
        new_block = hard_block.HardBlock()
        new_block.goto(x, 275)
        master_block.list_of_blocks.append(new_block)
        master_block.list_of_hard_blocks.append(new_block)

        new_block = top_block.TopBlock()
        new_block.goto(x, 300)
        master_block.list_of_blocks.append(new_block)
        master_block.list_of_top_blocks.append(new_block)
        new_block = top_block.TopBlock()
        new_block.goto(x, 325)
        master_block.list_of_blocks.append(new_block)
        master_block.list_of_top_blocks.append(new_block)


# Set starting block arrangement and scoreboard
set_starting_blocks()
scoreboard.update_board()

# Keep track of destroyed blocks.
list_of_destroyed_blocks = []

# Set screen event listeners.
screen.listen()
screen.onkeypress(bar.move_left, 'Left')
screen.onkeypress(bar.move_right, 'Right')

# Main game loop.
game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # If ball collides with the wall, bounce away.
    if ball.xcor() > 450 or ball.xcor() < -450:
        ball.bounce_x()
    if ball.ycor() > 350:
        ball.bounce_y()

    # If ball collides with the bar, bounce away
    if ball.distance(bar) < 85 and -280 > ball.ycor() > -300:
        ball.bounce_y()

    # If the user bar misses the ball, the ball resets in the middle of the screen.
    if ball.ycor() < -370:
        ball.reset_pos()
        scoreboard.lose_life()

    # Detect collision with blocks, then add points and change speed if necessary.
    for block in master_block.list_of_blocks:
        if ball.distance(block) < 20 and block.isvisible():
            ball.bounce_y()
            block.break_on_contact()
            list_of_destroyed_blocks.append(block)
            scoreboard.gain_points(block.points_given)
            if block in master_block.list_of_easy_blocks and ball.speed_level < 2:
                ball.ball_speed = ball.easy_speed
                ball.speed_level = 2
            elif block in master_block.list_of_medium_blocks and ball.speed_level < 3:
                ball.ball_speed = ball.medium_speed
                ball.speed_level = 3
            elif block in master_block.list_of_hard_blocks and ball.speed_level < 4:
                ball.ball_speed = ball.hard_speed
                ball.speed_level = 4
            elif block in master_block.list_of_top_blocks and ball.speed_level < 5:
                ball.ball_speed = ball.top_speed
                ball.speed_level = 5

    # Resets the blocks if the user destroyed them all.
    if len(list_of_destroyed_blocks) == len(master_block.list_of_blocks):
        master_block.reset_blocks()
        set_starting_blocks()
        list_of_destroyed_blocks = []
        ball = Ball()

    # Game ends when user lives run out.
    if scoreboard.lives_left == 0:
        scoreboard.show_game_over()
        game_on = False

screen.exitonclick()
