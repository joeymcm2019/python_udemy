from turtle import Turtle
from random import randint

directions = {
    "down-right": 45,
    "down-left": 45+90,
    "up-left": 45+180,
    "up-right": 45+270
}

starting_directions = { #clockwise orientation
    0: 45,
    1: 45+90,
    2: 45+180,
    3: 45+270
}

screen_height = 600
screen_width = 800


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=-40,y=0)
        self.shape("circle")
        self.shapesize(stretch_wid=20/21, stretch_len=20/21)
        rand_direction = starting_directions[randint(0,3)]
        self.direction = rand_direction
        self.ball_speed = 1.40 #how much we move the ball for each render

    def reset_ball(self):
        self.goto(x=-40, y=0)
        rand_direction = starting_directions[randint(0,3)]
        self.direction = rand_direction
        self.ball_speed = 1.20


    def move_ball(self):
        xcor = self.xcor()
        ycor = self.ycor()
        ball_speed = self.ball_speed
        
        #top & bottom wall collisions
        if (ycor >= screen_height/2-13):
            if (self.direction == directions["up-right"]):
                self.direction = directions["down-right"]
            elif (self.direction == directions["up-left"]):
                self.direction = directions["down-left"]

        elif (ycor <= -screen_height/2+20):
            if (self.direction == directions["down-right"]):
                self.direction = directions["up-right"]
            elif (self.direction == directions["down-left"]):
                self.direction = directions["up-left"]

        #ball movement
        if self.direction == directions["down-right"]:
            self.goto(x=xcor+ball_speed, y=ycor-ball_speed)

        elif self.direction == directions["down-left"]:
            self.goto(x=xcor-ball_speed, y=ycor-ball_speed)

        elif self.direction == directions["up-left"]:
            self.goto(x=xcor-ball_speed, y=ycor+ball_speed)

        elif self.direction == directions["up-right"]:
            self.goto(x=xcor+ball_speed, y=ycor+ball_speed)


    def bounce_off_left_paddle(self):
        if (self.direction == directions["down-left"]):
            self.direction = directions["down-right"]
        elif (self.direction == directions["up-left"]):
            self.direction = directions["up-right"]
        self.increase_ball_speed()

    def bounce_off_right_paddle(self):
        if (self.direction == directions["up-right"]):
            self.direction = directions["up-left"]
        elif (self.direction == directions["down-right"]):
            self.direction = directions["down-left"]
        self.increase_ball_speed()

    def increase_ball_speed(self):
        self.ball_speed += .075