from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.clear()
        self.score = 0
        self.write(f"level: {self.score}", False, align=ALIGNMENT, font=FONT)

    def scorepoint(self):
        self.clear()
        self.score += 1
        self.write(f"level: {self.score}", False, align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", False, align=ALIGNMENT, font=FONT)

