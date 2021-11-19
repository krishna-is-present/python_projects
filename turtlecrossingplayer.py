from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(UP)

    def startagain(self):
        self.goto(0, -280)
        self.setheading(UP)
        self.shape("turtle")
        self.penup()

    def up(self):
        self.forward(10)
