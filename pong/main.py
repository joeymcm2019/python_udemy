from turtle import Turtle, Screen
from gameboard import Gameboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


gameboard = Gameboard()
screen.update()

screen.exitonclick()
