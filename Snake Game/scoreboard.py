from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        # self.goto(x=0, y=270)
        self.hideturtle()
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(x=0, y=270)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(x=0, y=250)
        self.write(f"High Score : {self.highscore}", align=ALIGNMENT, font=FONT)

    def new_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def high_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.show_score()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(f"Game Over.", align=ALIGNMENT, font=FONT)