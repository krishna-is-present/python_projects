from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-180, -120, -60, 0, 60, 120]
turtles = []

def position():
    for index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_position[index])
        new_turtle.color(colors[index])
        turtles.append(new_turtle)

position()

if user_bet:
    race_is_on = True

while race_is_on:
    for single_turtle in turtles:
        single_turtle.forward(random.randint(0, 10))
        if single_turtle.xcor() >= 150.0:
            if single_turtle.pencolor() == user_bet:
                print(f"You Won. \nGame is over. \n{single_turtle.pencolor()} color turtle won")
            else:
                print(f"You lost. \nGame is over. \n{single_turtle.pencolor()} color turtle won")
            race_is_on = False


