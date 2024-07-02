from turtle import Turtle

COORDINATES = [(0, 0), (0, -20), (0, -40)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in COORDINATES:
            self.increase_size(position)

    def increase_size(self, position):
        alen = Turtle(shape="square")
        alen.color("white")
        alen.penup()
        alen.goto(position)
        self.segments.append(alen)

    def add_size(self):
        self.increase_size(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(x=1000, y=1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
