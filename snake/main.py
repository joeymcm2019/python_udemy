from turtle import Turtle, Screen
import time
from food import Food
from score import Score
from gameover import Gameover

screen = Screen()
screen.bgcolor("black")
screen_size = 600
screen.setup(width=screen_size, height=screen_size)
screen.title("Snake")
screen.tracer(0)

snake = []
snake_size = 5
snake_part_direction = []
snake_part_next_direction = []
snake_part_width = 20

#initialize snake body
for i in range (0, snake_size, 1):
    snake_part = Turtle()
    snake_part.shape("square")
    snake_part.color("white")
    xcor = snake_part.xcor()
    snake_part.penup()
    snake_part.setx(xcor-i*snake_part_width)
    snake.append(snake_part)
    snake_part_direction.append("right")
    snake_part_next_direction.append("right")
    

directions = {
    "right": 0,
    "up": 90,
    "left": 180,
    "down": 270
}

def move_snake():
    snake_len = len(snake)
    for i in range(0, snake_len, 1):
        snake_part_direction[i] = snake_part_next_direction[i]
        snake[i].setheading(directions[snake_part_direction[i]])
        if i != 0:
            snake_part_next_direction[i] = snake_part_direction[i-1]
        snake[i].forward(snake_part_width)
    time.sleep(.1)
    screen.update()
    
game_is_on = True


def set_direction_right():
    if (snake_part_direction[0] != "left"):
        snake_part_next_direction[0] = "right"

def set_direction_down():
    if (snake_part_direction[0] != "up"):
        snake_part_next_direction[0] = "down"

def set_direction_left():
    if (snake_part_direction[0] != "right"):
        snake_part_next_direction[0] = "left"

def set_direction_up():
    if (snake_part_direction[0] != "down"):
        snake_part_next_direction[0] = "up"


screen.listen()
screen.onkey(key="Right", fun=set_direction_right)
screen.onkey(key="d", fun=set_direction_down)
screen.onkey(key="Up", fun=set_direction_up)
screen.onkey(key="Left", fun=set_direction_left)
screen.onkey(key="Down", fun=set_direction_down)

food = Food()
food_coord = (food.xcor(), food.ycor())


def is_out_of_bounds(turtle):
    if abs(turtle.xcor()) >= screen_size/2 or abs(turtle.ycor()) >= screen_size/2:
        return True
    
def collectedFood():
    if (snake[0].distance(food) < 10):
        return True

def get_new_part_coord(xcor, ycor, snake_part_direction):
    if snake_part_direction == "down":
        ycor += 20
    elif snake_part_direction == "up":
        ycor -= 20
    elif snake_part_direction == "right":
        xcor -= 20
    elif snake_part_direction == "left":
        xcor += 20
    return (xcor, ycor)        

def make_snake_grow():
    snake_len = len(snake)
    snake_part = Turtle()
    snake_part.shape("square")
    snake_part.color("white")
    xcor = snake[snake_len-1].xcor()
    ycor = snake[snake_len-1].ycor()
    snake.append(snake_part)
    snake_part.penup()
    snake_part_direction.append(snake_part_next_direction[snake_len-1])
    snake_part_next_direction.append(snake_part_next_direction[snake_len-1])
    snake_len = len(snake)
    (xcor, ycor) = get_new_part_coord(xcor, ycor, snake_part_direction[snake_len-1])
    snake_part.goto(x=round(xcor,0), y=round(ycor,0))

def collision_with_self():
    for part in snake[1:]:
        if snake[0].distance(snake[i]) < 10:
            return True
    return False

score = Score()

while game_is_on:
    screen.update()
    move_snake()
    if is_out_of_bounds(snake[0]):
        game_is_on = False
        pass
    elif collision_with_self():
        game_is_on = False
    elif collectedFood():
        make_snake_grow()
        score.update_score()
        food.set_new_coord(snake)

def clear_screen():
    food.hideturtle()
    score.clear()
    for part in snake:
        part.hideturtle()
    screen.update()

clear_screen()
end_screen = Gameover(score.score)
screen.update()

screen.exitonclick()


