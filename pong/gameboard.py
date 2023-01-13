from turtle import Turtle

screen_width = 800
screen_height = 600

class Gameboard:

    def __init__(self):
        num_border_parts = int(round(screen_height/40,0))-1
        for i in range(0, num_border_parts, 1):
            middle_border_part = Turtle()
            middle_border_part.penup()
            middle_border_part.color("white")
            middle_border_part.shape("square")
            xcor = middle_border_part.xcor()
            ycor = -screen_height/2+i*40+40
            middle_border_part.goto(x=xcor, y=ycor)
