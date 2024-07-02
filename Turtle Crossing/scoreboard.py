from turtle import Turtle
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.level_up()

    def level_up(self):
        self.clear()
        self.goto(x=-240, y=260)
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def level_value(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

