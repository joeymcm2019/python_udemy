from turtle import Screen
from gameboard import Gameboard
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
from instruction import Instruction

screen = Screen()
screen_width = 800
screen_height = 600
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.tracer(0)



scoreboard = Scoreboard()

player_one_paddle = Paddle(-screen_width/2+13)
player_two_paddle = Paddle(screen_width/2-20)

def move_player_one_paddle_up():
    if (int(round(player_one_paddle.ycor())) < screen_height/2-55):
        player_one_paddle.setheading(90)
        player_one_paddle.forward(20)
        screen.update()

def move_player_one_paddle_down():
    if (int(round(player_one_paddle.ycor())) > -screen_height/2+60):
        player_one_paddle.setheading(270)
        player_one_paddle.forward(20)
        screen.update()

def move_player_two_paddle_up():
    if (int(round(player_two_paddle.ycor())) < screen_height/2-55):
        player_two_paddle.setheading(90)
        player_two_paddle.forward(20)
        screen.update()

def move_player_two_paddle_down():
    if (int(round(player_two_paddle.ycor())) > -screen_height/2+60):
        player_two_paddle.setheading(270)
        player_two_paddle.forward(20)
        screen.update()

screen.listen()
screen.onkeypress(key="w", fun=move_player_one_paddle_up)
screen.onkeypress(key="s", fun=move_player_one_paddle_down)
screen.onkeypress(key="Up", fun=move_player_two_paddle_up)
screen.onkeypress(key="Down", fun=move_player_two_paddle_down)

ball = Ball()

def collision_with_left_paddle():
    if ball.distance(player_one_paddle) <= 50:
        return True

def collision_with_right_paddle():
    if ball.distance(player_two_paddle) <= 50:
        return True

def award_point_to_player_one():
    scoreboard.add_point_to_player_one()

def award_point_to_player_two():
    scoreboard.add_point_to_player_two()



instructions = []

def write_instructions():
    instructions.append(Instruction("Player One: w=up s=down", 0))
    instructions.append(Instruction("Player Two: ↑=up ↓=down", 1))
    instructions.append(Instruction("Press space to play, enter to quit",2))
    

def clear_instructions():
    for instruction in instructions:
        instruction.clear()

ball_is_in_play = False

def begin_play():
    global ball_is_in_play
    ball_is_in_play = True
    clear_instructions()

screen.onkeypress(key="space", fun=begin_play)

def quit_game():
    if (not(ball_is_in_play)):
        screen.bye()

screen.onkeypress(key="Return", fun=quit_game)

game_is_on = True

gameboard = Gameboard()
write_instructions()


while (game_is_on):
    if (ball_is_in_play):
        ball.move_ball()        
    
    ball_xcor = ball.xcor()
   
    if (ball_xcor <= -screen_width/2+32):
        #print(ball.distance(player_one_paddle))
        if (ball_xcor >= -screen_width/2):
            if (collision_with_left_paddle()):
                ball.bounce_off_left_paddle()
        elif (ball_xcor < -screen_width/2):
            award_point_to_player_two()
            ball_is_in_play = False
            ball.reset_ball()
    elif (ball_xcor >= screen_width/2-32):
        #print(ball.distance(player_two_paddle))
        if (ball_xcor <= screen_width/2):
            if (collision_with_right_paddle()):
                ball.bounce_off_right_paddle()
        elif (ball_xcor > screen_width/2):
            award_point_to_player_one()
            ball_is_in_play = False
            ball.reset_ball()
            

    screen.update()



screen.exitonclick()
