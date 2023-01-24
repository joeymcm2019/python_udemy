from turtle import Turtle
from highscore import get_high_score

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = get_high_score()
        msg = 'score: '
        self.color("white")
        self.penup()
        self.goto(x=0, y=280)
        self.hideturtle()
        self.write(f"score: {self.score} highscore: {self.highscore}", move=False, align="center", font=("Arial", 12, "normal"))
       
        
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"score: {self.score} highscore: {self.highscore}", move=False, align="center", font=("Arial", 12, "normal"))


