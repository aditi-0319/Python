from turtle import Turtle
import random
LENGTH = 0.5
WIDTH = 0.5


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=LENGTH, stretch_wid=WIDTH)
        self.color("blue")
        self.speed("fastest")
        self.new_food_location()

    def new_food_location(self):
        x_random = random.randint(-280, 280)
        y_random = random.randint(-280, 280)
        self.goto(x=x_random, y=y_random)