import turtle
from turtle import Turtle, Screen
import random

game_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Choose a color out of red, orange, yellow, green, blue or purple")
position = [125, 75, 25, -25, -75, -125]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in range(6):
    alen = Turtle(shape="turtle")
    alen.color(colors[i])
    alen.penup()
    alen.goto(x=-220, y=position[i])
    turtles.append(alen)

if user_input:
    game_on = True

while game_on:
    for n in turtles:
        if n.xcor() > 230:
            game_on = False
            winner = n.pencolor()
            if user_input == winner:
                print(f"You've won! The color {winner} won the race.")
            else:
                print(f"You've lost! The color {winner} won the race.")

        distance = random.randint(1, 12)
        n.forward(distance)

screen.exitonclick()