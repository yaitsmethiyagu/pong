from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.y_move = random.randrange(7, 15)
        self.x_move = random.randrange(7, 15)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # print(self.xcor())

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.setposition(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1
        # self.y_move = random.randrange(7, 15)
