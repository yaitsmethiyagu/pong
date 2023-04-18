from turtle import Turtle

SPEED = 20
SCREEN_EDGE = 230

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(x, y)
        self.xloc = x
        self.yloc = y

    def up(self):
        yaxis = self.ycor()
        if yaxis < SCREEN_EDGE:
            self.goto(self.xloc, yaxis + SPEED)

    def down(self):
        yaxis = self.ycor()
        if yaxis > - SCREEN_EDGE:
            self.goto(self.xloc, yaxis - SPEED)