from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

SCORE_POINTS = 1

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
l_score = Score("left")
r_score = Score("right")

screen.listen()

screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")
screen.tracer(1)
while True:
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 390:
        print("left score")
        l_score.update_score(SCORE_POINTS)
        # time.sleep(2)
        ball.reset()
        time.sleep(1)

    if ball.xcor() < -390:
        print("right score")
        r_score.update_score(SCORE_POINTS)
        # time.sleep(2)
        ball.reset()
        time.sleep(1)

    screen.update()

screen.exitonclick()
