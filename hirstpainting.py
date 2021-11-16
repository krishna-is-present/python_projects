import colorgram
import turtle as tim
import random

tim.colormode(255)
t = tim.Turtle()

color_list = [ (214, 157, 85), (33, 105, 151), (238, 215, 94), (153, 75, 52), (125, 168, 199), (209, 134, 163), (156, 60, 81), (22, 39, 54), (212, 85, 61), (176, 162, 47), (200, 85, 119), (135, 184, 150), (56, 119, 90), (240, 213, 4), (25, 46, 37), (228, 167, 186), (64, 46, 34), (87, 157, 100), (9, 99, 75), (34, 166, 189), (40, 60, 102), (228, 175, 166), (179, 189, 213), (95, 126, 173), (68, 34, 44), (105, 42, 60), (170, 205, 179), (113, 43, 37), (156, 206, 217), (78, 69, 35), (3, 90, 115)]
t.speed(0)


def draw():
    t.pendown()
    t.color(random.choice(color_list))
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.penup()
    t.forward(80)

def line():
    for _ in range(10):
        draw()

angle = 0

def paint():
    global angle
    for _ in range(10):
        line()
        angle += 50
        t.setx(0)
        t.sety(angle)
        
        
paint()

screen = tim.Screen()
screen.exitonclick()
