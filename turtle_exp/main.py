from turtle import Turtle, Screen
from random import random
from random import randint
import colorgram

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.penup()
timmy.setx(-200)
timmy.sety(-200)
timmy.pendown()
timmy.pensize(1)
timmy.speed("fastest")
my_screen = Screen()
print(my_screen.canvheight)

def makeAsquare(turtle):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)


#makeAsquare(timmy)
def makeDashedLine(turtle):
    for x in range(1,10,1):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

my_screen.colormode(255)

def makeShape(turtle, baseLength, numSides, color):
    pass
    turtle.pencolor(color)
    angleToTurn = 180 - round((numSides-2)*180/numSides, 2)
    for x in range(0,numSides,1):
        turtle.forward(baseLength)
        turtle.right(angleToTurn)


def getRandomColor():
    randRed = int(round((random()*255),0))
    randGreen = int(round((random()*255),0))
    randBlue = int(round((random()*255),0))
    return (randRed, randGreen, randBlue)

def getRandomDistance():
    return int(round((random()*100),0))

def makeAlotOfShapes(turtle):
    for x in range(3, 11, 1):
        randColor = getRandomColor()    
        makeShape(turtle, 100, x, randColor)

def getRandomDirection():
    rand = int(round((random()*3),0))
    if (rand == 0):
        return 0
    elif (rand == 1):
        return 90
    elif (rand == 2):
        return 180
    elif (rand == 3):
        return 270
    else:
        print("rand out of range", rand)

def drawRandomWalk(turtle):
    for x in range(0,50,1):
        randColor = getRandomColor()
        randDist = getRandomDistance()
        randDirection = getRandomDirection() 
        turtle.right(randDirection)
        turtle.color(randColor)
        turtle.forward(randDist)


def drawCircle(turtle, circleSize):
    color = getRandomColor()
    turtle.color(color)
    turtle.circle(circleSize)

def drawSpirograph(turtle, numberOfCircles):
    for x in range (0, numberOfCircles, 1):
        drawCircle(turtle, 100)
        turtle.right(360/numberOfCircles)
    timmy.penup()
    timmy.forward(200)


# drawSpirograph(timmy, 60)



colors = colorgram.extract("hirst-painting.jpg", 10)

def getRandomHirstColor(colors):
    randInt = randint(0,9)
    red = colors[randInt].rgb.r
    green = colors[randInt].rgb.g
    blue = colors[randInt].rgb.b
    return (red,green,blue)

def makeHirstPainting(turtle):
    for x in range(0, 10, 1):
        drawHirstRow(turtle, row=x)

def drawHirstRow(turtle, row):
    turtle.penup()
    turtle.setx(-200)
    turtle.sety(row*40-200)
    turtle.pendown()
    for x in range(0, 10, 1):
        turtle.dot(20, getRandomHirstColor(colors))
        turtle.penup()
        turtle.forward(40)
        turtle.pendown()

makeHirstPainting(timmy)

my_screen.exitonclick()
print("done")

