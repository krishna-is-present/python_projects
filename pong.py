from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()

screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.sleep_time)
    screen.update()
    ball.move()

    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 325 or ball.distance(paddle_l) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.ball_reset()
        score.scoretrack_player_l()

    if ball.xcor() < -380:
        ball.ball_reset()
        score.scoretrack_player_r()

screen.exitonclick()
