import turtle as t
import colorgram
import random

alen = t.Turtle()
alen.hideturtle()
alen.screen.bgcolor("powder blue")
t.colormode(255)

colors = colorgram.extract('image.jpg', 30)

color_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    item = (r, g, b)
    color_list.append(item)

# color_list = [(253, 253, 251), (243, 252, 249), (253, 246, 250), (236, 245, 251), (214, 152, 112), (28, 104, 180), (163, 82, 45), (179, 12, 33), (118, 171, 209), (216, 132, 161), (239, 223, 99), (220, 67, 102), (157, 57, 96), (230, 76, 46), (20, 51, 147), (73, 24, 11), (122, 184, 141), (174, 148, 30), (16, 170, 206), (47, 184, 132), (235, 165, 181), (134, 229, 194), (41, 127, 80), (236, 169, 159), (151, 26, 18), (12, 25, 84), (87, 108, 194), (77, 21, 36), (127, 213, 233), (173, 185, 225)]

alen.speed("fastest")

alen.penup()
alen.setheading(225)
alen.forward(300)
alen.setheading(0)


def dots():
    for _ in range(0, 10):
        alen.dot(20, random.choice(color_list))
        alen.penup()
        alen.forward(50)


def going_up():
    alen.setheading(90)
    alen.forward(50)
    alen.setheading(180)
    alen.forward(500)
    alen.setheading(0)


dots()
for _ in range(9):
    going_up()
    dots()

screen = t.Screen()
screen.exitonclick()