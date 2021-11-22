import turtle
import pandas
import pandas as pd

screen = turtle.Screen()
#screen.tracer(0)
screen.title("U.S STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
a = 0
isTrue = True
data = pandas.read_csv("50_states.csv")
print(type(data.state))
states_missed = pandas.read_csv("50_states.csv")
while isTrue:
    answer_state = screen.textinput(title="Guess the State", prompt= "What's the another state name? ")

    if answer_state == "exit":
        break

    data = pandas.read_csv("50_states.csv")
    states = data[data.state == answer_state]
    if states.empty:
        continue
    states_missed = states_missed[data.state != answer_state]
    x_axis = float(states.x)
    y_axis = float(states.y)
    figure = str(states.state)

    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(x_axis, y_axis)
    new_turtle.clear()
    new_turtle.write(answer_state)
    a += 1
    if a > 50:
        isTrue == False


states_missed.to_csv("Missed_states.csv")



turtle.mainloop()
