from turtle import Turtle
from highscore import save_high_score

class Gameover(Turtle):
    
    def __init__(self, score, highscore):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("White")
        self.write(f"Score: {score}", align="center", move=False, font=("Arial", 20, "normal"))
        if score > highscore:
            print("saving score")
            save_high_score(score)
