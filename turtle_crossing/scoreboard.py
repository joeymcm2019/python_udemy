from turtle import Turtle

FONT = ("Courier", 18, "normal")

screen_width = 600

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        xcor = -screen_width/2+20
        ycor = 0
        self.goto(x=xcor, y=ycor)
        self.write(f"Level {self.level}", align="left", font=FONT)

    def increase_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align="left", font=FONT)

    def restart(self):
        self.clear()
        self.level = 1
        self.write(f"Level {self.level}", align="left", font=FONT)
