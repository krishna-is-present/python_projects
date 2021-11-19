import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


carmanager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
sleep_time = 0.1

while game_is_on:
    co_x = 280
    co_y = -250
    time.sleep(sleep_time)
    screen.update()
    carmanager.addcars()
    carmanager.move()

    for segment in carmanager.cars:


        if segment.distance(player) < 20:
            scoreboard.gameover()
            game_is_on = False

    if player.ycor() > 250:
        scoreboard.scorepoint()
        carmanager.repeat()
        player.startagain()

screen.exitonclick()
