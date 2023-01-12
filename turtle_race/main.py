from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=500)

num_turtles_racing = 7
turtle_row_size = 40


window_width = screen.window_width()

colors = {
    0: "red",
    1: "yellow",
    2: "blue",
    3: "green",
    4: "purple",
    5: "orange",
    6: "magenta"
}

color_indexes = {
    "red": 0,
    "yellow": 1,
    "blue": 2,
    "green": 3,
    "purple": 4,
    "orange": 5,
    "magenta": 6
}

colors_array = ["red", "yellow", "blue", "green", "purple", "orange", "magenta"]

user_turtle_bet = screen.textinput("", "Enter the color of the turtle you'd like to bet on.")
if user_turtle_bet != None:
    user_turtle_bet = user_turtle_bet.lower()
if user_turtle_bet == "":
    user_turtle_bet = "invalid"
#print(user_turtle_bet)

user_turtle_bet_index = ""

def getRandomColor():
    randRed = randint(0,255)
    randGreen = randint(0,255)
    randBlue = randint(0,255)
    return (randRed, randGreen, randBlue)

def configure_turtle_for_race(turtle, index):
    turtle.speed(10)
    turtle.penup()
    turtle.shape("turtle")
    turtle.setx(-window_width/2+20)
    ycord = turtle.ycor()+turtle_row_size*num_turtles_racing/2  #center turtles
    turtle.sety(ycord-index*turtle_row_size)
    colorSelected = False
    global user_turtle_bet
    global user_turtle_bet_index
    while (colorSelected == False):
        if (index == num_turtles_racing-1 and not(colors_array.__contains__(user_turtle_bet))):
            turtle.color(colors[index])
            try:
                turtle.color(user_turtle_bet)
                colorSelected = True
                user_turtle_bet_index = index
            except: #invalid color
                colorSelected = False
                user_turtle_bet = screen.textinput("", "Please choose a valid color to be on (red, green, blue, etc)")
                if user_turtle_bet != None:
                    user_turtle_bet = user_turtle_bet.lower()
                if user_turtle_bet == "":
                    user_turtle_bet = "invalid"
        else:
            turtle.color(colors[index])
            colorSelected = True
            if (index == num_turtles_racing -1):
                user_turtle_bet_index = color_indexes[user_turtle_bet]
    #print(user_turtle_bet_index)
   


turtles = []
for i in range(0, num_turtles_racing, 1):
    new_turtle = Turtle()
    configure_turtle_for_race(new_turtle, i)
    turtles.append(new_turtle)
    #print(new_turtle.color()[0])



def execute_race_simulation():
    race_complete = False
    winning_turtle = ""
    while (not(race_complete)):
        for turtle in turtles:
            randForwardDist = randint(1,10)
            turtle.forward(randForwardDist)
            if (turtle.xcor() > window_width/2-10):
                winning_turtle = turtle
                race_complete = True
    winner = winning_turtle.color()[0]
    if (winner == user_turtle_bet):
        print(f"Turtle {winner} finished first. You won!")
    else: 
        print(f"Turtle {winner} won the race. Sorry, you lost!")

execute_race_simulation()


screen.exitonclick()
