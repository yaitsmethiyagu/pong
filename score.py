from turtle import Turtle

ALIGN = "center"
FONT = ("courier", 50, "normal")


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.current_position = position
        self.update_score(0)



    def update_score(self, points):
        self.score += points

        self.clear()
        if self.current_position == "left":
            self.goto(-150, 200)

        elif self.current_position == "right":
            self.goto(150, 200)
        self.write(f"{self.score}", move=True, align=ALIGN, font=FONT)
