from turtle import Turtle
from random import randint

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        invalid_coord = True
        while invalid_coord:
            random_x = randint(-14, 14)
            random_y = randint(-14, 14)
            if (random_y == 0):
                if (random_x == 0 or random_x == -1 or random_x == -2):
                    invalid_coord = True
                else:
                    invalid_coord = False
            else:
                invalid_coord = False
        self.goto(x=random_x*20, y=random_y*20)
            
    def set_new_coord(self, snake):
         invalid_placement = True
         while invalid_placement:
            random_x = randint(-14, 14)
            random_y = randint(-14, 14)
            self.goto(x=random_x*20, y=random_y*20)
            for part in snake:
                if self.distance(part) < 10:
                    invalid_placement = True
                    break
                else:
                    invalid_placement = False



