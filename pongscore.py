from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 40, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.scoretrack()

    def scoretrack(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.clear()
        self.write(f" {self.score1}     {self.score2}", False, align=ALIGNMENT, font=FONT)

    def scoretrack_player_l(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.clear()
        self.score1 += 1
        self.write(f" {self.score1}     {self.score2}", False, align=ALIGNMENT, font=FONT)

    def scoretrack_player_r(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 250)
        self.clear()
        self.score2 += 1
        self.write(f" {self.score1}     {self.score2}", False, align=ALIGNMENT, font=FONT)
