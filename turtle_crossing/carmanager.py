from car import Car
from random import randint
from speed import Speed

min_cars_in_col = 0
max_cars_in_col = 6

speed = Speed()
STARTING_SPEED = speed.starting_speed
SPEED_INCREMENT = speed.speed_increment

MAX_ROW_SPACING = 140
MIN_ROW_SPACING = 80


screen_width = 600

#handles a column of cars
class CarColManager(Car):

    def __init__(self, level):
        self.distance_moved = 0
        self.level = level
        added_speed = STARTING_SPEED*SPEED_INCREMENT*(level-1)
        self.speed = STARTING_SPEED + added_speed
        # don't need to save taken_left_lanes or taken_right lanes. 
        # I use these to make sure I don't put multiple cars in the same place
        taken_left_lanes = {
            0: False,
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
        }
        taken_right_lanes = {
            0: False,
            1: False,
            2: False,
            3: False,
            4: False,
            5: False,
        }

        self.left_cars = []
        self.right_cars = []
        self.cars = []
        
        self.num_cars_left = randint(min_cars_in_col, max_cars_in_col)
        for i in range(0, self.num_cars_left, 1):
            car_left = Car(direction="left", level=level, lanestaken=taken_left_lanes)
            taken_left_lanes[car_left.lane] = True
            self.left_cars.append(car_left)
            self.cars.append(car_left)
        
        self.num_cars_right = randint(min_cars_in_col, max_cars_in_col)
        for i in range(0, self.num_cars_right, 1):
            car_right = Car(direction="right", level=level, lanestaken=taken_right_lanes)
            taken_right_lanes[car_right.lane] = True
            self.right_cars.append(car_right)
            self.cars.append(car_right)
        

    def move_cars(self):
        for car in self.left_cars:
            car.move_car()
        for car in self.right_cars:
            car.move_car()
        self.distance_moved += self.speed

    def clear_cars(self):
        for car in self.left_cars:
            car.color("white")
            car.clear()
        for car in self.right_cars:
            car.color("white")
            car.clear()
        self.right_cars = []
        self.left_cars = []

    def move_off_screen(self):
        for car in self.left_cars:
            car.goto(800,800) #off screen
        for car in self.right_cars:
            car.goto(800,800)

    def update_speed(self):
        self.level += 1
        added_speed = STARTING_SPEED*SPEED_INCREMENT*(self.level-1)
        self.speed = STARTING_SPEED + added_speed
        for car in self.left_cars:
            car.update_speed()
        for car in self.right_cars:
            car.update_speed()
    
    def restart(self):
        self.level = 1
        added_speed = STARTING_SPEED*SPEED_INCREMENT*(self.level-1)
        self.speed = STARTING_SPEED + added_speed
        for car in self.left_cars:
            car.restart()
        for car in self.right_cars:
            car.restart()


#handles all the cars
class CarManager():

    def __init__(self):
        self.car_cols = []
        self.level = 1
        self.row_spacing = MAX_ROW_SPACING
        self.generate_cars()
        

    def generate_cars(self):
        car_col = CarColManager(level=self.level)
        self.car_cols.append(car_col)
        while car_col.distance_moved < 650:
            self.move_cars()

    def create_new_col(self):
        car_col = CarColManager(self.level)
        self.car_cols.append(car_col)
    
    def move_cars(self):
        i = 0 # need to know when I'm at the end of the loop
        for car_col in self.car_cols:
            num_car_cols = len(self.car_cols)
            car_col.move_cars()
             #once min distance is met allow player to move
            if car_col.distance_moved >= 750:  #cars went as far as they can go
                car_col.clear_cars()
                self.car_cols.pop(0)
                num_car_cols = len(self.car_cols) 
            elif i == num_car_cols - 1:
                if car_col.distance_moved >= self.row_spacing:
                    self.create_new_col()
            i += 1
    
    def next_level(self):
        for car_col in self.car_cols:
            car_col.update_speed()
        self.level += 1
        self.row_spacing -= 5
        if self.row_spacing < MIN_ROW_SPACING:
            self.row_spacing = MIN_ROW_SPACING

    def restart(self):
        for car_col in self.car_cols:
            car_col.restart()
        self.level = 1
