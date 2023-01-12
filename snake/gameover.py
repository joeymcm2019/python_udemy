from turtle import Turtle

class Gameover(Turtle):
    
    def __init__(self, score):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("White")
        self.write(f"Game Over. Final Score: {score}", align="center", move=False, font=("Arial", 20, "normal"))