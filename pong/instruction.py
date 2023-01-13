from turtle import Turtle

class Instruction(Turtle):

    def __init__(self, msg, index):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("blue")
        self.goto(x=50,y=-(index-1)*40-10)
        self.write(f"{msg}", move=False, align="left", font=("", 15, "normal"))
        
