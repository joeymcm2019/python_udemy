from turtle import Turtle

screen_height = 600

class Paddle(Turtle):

    def __init__(self, starting_x_pos):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.goto(x=starting_x_pos, y=0)