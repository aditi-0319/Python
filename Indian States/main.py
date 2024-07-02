import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("Guess the states and Union Territories")
image = "indian-map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("indian-list.csv")
name_list = data.State.to_list()
guess_list = []

while len(guess_list) < 36:
    answer = screen.textinput(title=f"{len(guess_list)}/36 names guessed",
                              prompt="What's your guess? (Type 'exit' to exit the game)")
    state_name = answer.title()

    if state_name == 'Exit':
        # missing_names = []
        # for name in name_list:
        #     if name not in guess_list:
        #         missing_names.append(name)

        missing_names = [name for name in name_list if name not in guess_list]
        new_data = pandas.DataFrame(missing_names)
        new_csv = new_data.to_csv("missed-states.csv", header=["state"], index=False)
        missed_csv = pandas.read_csv("missed-states.csv")

        for n in name_list:
            if n in missing_names:
                t = Turtle()
                t.color("red")
                t.shape("circle")
                t.shapesize(stretch_len=0.1, stretch_wid=0.1)
                screen.tracer(0)
                t.penup()
                name_data = data[data.State == n]
                t.goto(int(name_data.x), int(name_data.y))
                t.write(name_data.State.item(), align="center")
                screen.update()

        break

    if state_name in name_list:
        guess_list.append(state_name)
        alen = Turtle()
        alen.penup()
        alen.color("blue")
        alen.shape("circle")
        alen.shapesize(stretch_len=0.1, stretch_wid=0.1)
        # alen.hideturtle()
        name_data = data[data.State == state_name]
        alen.goto(int(name_data.x), int(name_data.y))
        alen.write(name_data.State.item(), align="center")

# Q. How to get the coordinates for the states?
#
# def coordinates(x, y):
#     print(x, y)
#
# turtle.onscreenclick(coordinates)
# turtle.mainloop()
screen.exitonclick()
