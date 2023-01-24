from turtle import Screen
from player import Player
from carmanager import CarManager
from scoreboard import Scoreboard
from instruction import Instruction

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = CarManager()
player = Player()
screen.title("Turtle Crossing")


game_is_on = True
allow_game_play = False
collision_occurred = False


def close_game():
    global game_is_on
    game_is_on = False
    screen.bye()

def start_level():
    player.reset()
    global collision_occurred
    collision_occurred = False
    global allow_game_play
    allow_game_play = True
    clear_instrictions()

screen.listen()
screen.onkeypress(key="Return", fun=close_game)
screen.onkeypress(key="space", fun=start_level)

instructions = []

def write_instructions():
        instructions.append(Instruction("Press space to start level.", 0))
        instructions.append(Instruction("Use w or ↑ to move turtle up.", 1))
        instructions.append(Instruction("Press enter to quit", 2))

def clear_instrictions(): 
    for instruction in instructions:
        instruction.clear()

write_instructions()

screen.update()


scoreboard = Scoreboard()



def write_game_over_instructions():
    instructions.append(Instruction(f"Game Over", .5))
    instructions.append(Instruction("space: restart game, enter: quit.", 1))
    

def game_over():
    global allow_game_play
    allow_game_play = False
    global collision_occurred
    collision_occurred = True
    write_game_over_instructions()
    cars.restart()
    scoreboard.restart()

collision_threshold = 15.0
collision_ycor_offset = 5

def collision():
    for car_col in cars.car_cols:
        for car in car_col.cars:
            if car.xcor() < 100 and car.xcor() > -100:
                x_distance = abs(player.xcor() - car.xcor())
                y_distance = abs(player.ycor() + collision_ycor_offset - car.ycor())
                if x_distance <= collision_threshold and y_distance <= collision_threshold:
                    print(x_distance, y_distance)
                    return True
            else:
                break
    


def move_player():
    global allow_game_play
    if (allow_game_play):
            if (player.move_player_check_if_done()): #level completed
                scoreboard.increase_score()
                cars.next_level()
                allow_game_play = False
                write_instructions()
            elif (collision()):
                game_over()
            
    

screen.onkey(key="w", fun=move_player)
screen.onkey(key="Up", fun=move_player)

while (game_is_on):
    if (not(collision_occurred)):             
        cars.move_cars()
    if collision(): 
        game_over()
    screen.update()

screen.exitonclick()
