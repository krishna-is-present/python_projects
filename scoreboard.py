from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.scoretrack()

    def scoretrack(self):
        self.score += 1
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, align=ALIGNMENT, font=FONT)
