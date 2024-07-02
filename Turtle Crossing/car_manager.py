from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 4


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.total_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            alen = Turtle()
            alen.shape("square")
            alen.shapesize(stretch_wid=1, stretch_len=2)
            alen.color(random.choice(COLORS))
            alen.penup()
            new_y = random.randint(-230, 250)
            alen.goto(x=320, y=new_y)
            alen.setheading(180)
            self.total_cars.append(alen)

    def move(self):
        for car in self.total_cars:
            car.forward(self.car_speed)

    def up_speed(self):
        self.car_speed += MOVE_INCREMENT
        self.speed(self.car_speed)

