import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
screen.onkeypress(player.move_forward, 'w')
cars.AMOUNT_OF_CARS = int(screen.textinput(title="Pick a difficulty", prompt="1-5 (5 is the easiest)"))
screen.listen()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.add_cars()
    cars.cars_move()
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.clear()
        scoreboard.update_level()
        scoreboard.show_level()
        cars.cars_speed_up()


    for car in cars.cars:
        if player.distance(car) < 18:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()