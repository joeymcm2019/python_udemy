from turtle import Turtle
from random import randint
from speed import Speed

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


speed = Speed()
STARTING_SPEED = speed.starting_speed
SPEED_INCREMENT = speed.speed_increment

screen_height = 600
screen_width = 600

MAX_OFFSET = 100
MIN_OFFSET = 60

left_traffic_lanes = {
    0: screen_height/2-50,
    1: screen_height/2-90,
    2: screen_height/2-130,
    3: screen_height/2-170,
    4: screen_height/2-210,
    5: screen_height/2-250,
}

right_traffic_lanes = {
    0: -screen_height/2+60,
    1: -screen_height/2+100,
    2: -screen_height/2+140,
    3: -screen_height/2+180,
    4: -screen_height/2+220,
    5: -screen_height/2+260,
}

NUM_TRAFFIC_LANES = 6

NUM_COLORS = 6

#find random open lane. If spot is taken, go to next available open spot
#I think randint might slow the program down, so I'm only calling that function once
def get_random_lane(lanestaken):
    rand_lane = randint(0,NUM_TRAFFIC_LANES-1)

    # modularly go through dictionary till we find opening
    while (lanestaken[rand_lane%(NUM_TRAFFIC_LANES)]):
        rand_lane += 1
    return rand_lane%(NUM_TRAFFIC_LANES)

class Car(Turtle):
    
    def __init__(self, direction, level, lanestaken):
        super().__init__()
        self.level = level
        self.penup()
        rand_color_index = randint(0,NUM_COLORS-1)
        self.color(COLORS[rand_color_index])
        self.shape("circle")
        added_speed = STARTING_SPEED*SPEED_INCREMENT*(level-1)
        self.speed = STARTING_SPEED + added_speed
        self.offset = MAX_OFFSET - level*5
        if self.offset < MIN_OFFSET:
            self.offset = MIN_OFFSET

        rand_lane = get_random_lane(lanestaken)
        self.lane = rand_lane
        rand_x_offset = randint(0, self.offset) #make traffic look random
        
        if (direction == "left"):
            ycor = left_traffic_lanes[rand_lane]
            self.goto(x=screen_width/2+60+rand_x_offset, y=ycor)
            self.setheading(180)
        
        elif (direction == "right"):
            ycor = right_traffic_lanes[rand_lane]
            self.goto(x=-screen_width/2-60-rand_x_offset, y=ycor)
    
    def move_car(self):
        self.forward(self.speed)

    def update_speed(self):
        self.level += 1
        added_speed = STARTING_SPEED*SPEED_INCREMENT*(self.level-1)
        self.speed = STARTING_SPEED + added_speed

    def restart(self):
        self.level = 1
        added_speed = STARTING_SPEED*SPEED_INCREMENT*(self.level-1)
        self.speed = STARTING_SPEED + added_speed
