import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=player.up, key='Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Creating a new car every refresh
    car_manager.create_car()
    car_manager.move_cars()

    # Check collision with top wall.
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_score()
        car_manager.level_up()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
