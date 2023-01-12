from turtle import Turtle, Screen

tim = Turtle()
# tim.shape("turtle")
# tim.color("blue")
screen = Screen()

def move_forwards():
    tim.forward(5)

def move_backwards():
    tim.backward(5)

def turn_clockwise():
    tim.right(5)

def turn_counter_clockwise():
    tim.left(5)

def do_circle():
    tim.right(5)
    tim.forward(5)


def reset_sketch():
    screen.reset()

screen.listen()



# w = forwards, s = backwards, a = turn counter-clockwise, d = turn clockwise, c = clear drawing
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="d", fun=turn_clockwise)
screen.onkeypress(key="a", fun=turn_counter_clockwise)
screen.onkeypress(key="c", fun=reset_sketch)

screen.exitonclick()