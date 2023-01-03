import random
from turtle import Turtle
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.cars = []
        self.STARTING_MOVE_DISTANCE = 5
        self.AMOUNT_OF_CARS = 2


    def add_cars(self):
        if random.randint(0, self.AMOUNT_OF_CARS) == 1:
            for _ in range(1):
                random_car = Turtle("square")
                random_car.pu()
                random_car.color(random.choice(COLORS))
                random_car.shapesize(stretch_wid=1, stretch_len=2)
                random_car.goto(300, random.randint(-255, 280))
                self.cars.append(random_car)


    def cars_move(self):
        for cars in self.cars:
            cars.backward(self.STARTING_MOVE_DISTANCE)

    def cars_speed_up(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT



