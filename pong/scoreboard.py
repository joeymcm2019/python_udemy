from turtle import Turtle

screen_height = 600

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_one_score = 0
        player_one_score_graphic = Turtle()
        player_one_score_graphic.penup()
        player_one_score_graphic.hideturtle()
        player_one_score_graphic.color("white")
        ycor = screen_height/2-70
        player_one_score_graphic.goto(x=-80, y=ycor)
        player_one_score_graphic.write(f"{self.player_one_score}", move=False, font=("", 40, "normal"))
        self.player_one_graphic = player_one_score_graphic

        self.player_two_score = 0
        player_two_score_graphic = Turtle()
        player_two_score_graphic.penup()
        player_two_score_graphic.hideturtle()
        player_two_score_graphic.color("white")
        ycor = screen_height/2-70
        player_two_score_graphic.goto(x=50, y=ycor)
        player_two_score_graphic.write(f"{self.player_two_score}", move=False, font=("", 40, "normal"))
        self.player_two_graphic = player_two_score_graphic

    def add_point_to_player_one(self):
        self.player_one_score += 1
        self.player_one_graphic.clear()
        self.player_one_graphic.write(f"{self.player_one_score}", move=False, font=("", 40, "normal"))

    def add_point_to_player_two(self):
        self.player_two_score += 1
        self.player_two_graphic.clear()
        self.player_two_graphic.write(f"{self.player_two_score}", move=False, font=("", 40, "normal"))