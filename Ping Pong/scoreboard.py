from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-330, 230)
        self.write(f"Left Player : {self.left_score}", align="center", font=("Arial", 20, "normal"))
        self.goto(310, 230)
        self.write(f"Right Player : {self.right_score}", align="center", font=("Arial", 20, "normal"))

    def left_point(self):
        self.left_score += 1
        self.update()

    def right_point(self):
        self.right_score += 1
        self.update()