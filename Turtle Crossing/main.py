import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")
screen.onkeyrelease(player.stop, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move()

    for each_car in car.total_cars:
        if each_car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

        if player.finish_line():
            player.start()
            car.up_speed()
            scoreboard.level_value()
            scoreboard.level_up()

screen.exitonclick()
