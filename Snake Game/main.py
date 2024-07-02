from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

DELAY = 3

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

counter = Turtle()
counter.penup()
counter.hideturtle()
counter.color("white")
counter.goto(0, 0)

for i in range(DELAY, 0, -1):
    counter.clear()
    counter.write(f"Game starts in {str(i)}", align="center", font=("Arial", 16, "normal"))
    screen.update()
    time.sleep(1)

counter.clear()
counter.write("GO!", align="center", font=("Arial", 16, "normal"))
screen.update()
time.sleep(1)
counter.clear()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.new_food_location()
        snake.add_size()
        scoreboard.new_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        for i in range(DELAY, 0, -1):
            counter.clear()
            counter.write(f"Game Over. New game starts in {str(i)}", align="center", font=("Arial", 16, "normal"))
            screen.update()
            time.sleep(1)

        counter.clear()
        counter.write("GO!", align="center", font=("Arial", 16, "normal"))
        screen.update()
        time.sleep(1)
        counter.clear()

        scoreboard.high_score()
        snake.reset()
        # game_on = False
        # scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            for i in range(DELAY, 0, -1):
                counter.clear()
                counter.write(f"Game Over. New game starts in {str(i)}", align="center", font=("Arial", 16, "normal"))
                screen.update()
                time.sleep(1)

            counter.clear()
            counter.write("GO!", align="center", font=("Arial", 16, "normal"))
            screen.update()
            time.sleep(1)
            counter.clear()

            scoreboard.high_score()
            snake.reset()
            # game_on = False
            # scoreboard.game_over()

screen.exitonclick()
