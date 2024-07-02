from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=900)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

left_paddle = Paddle((-400, 0))
right_paddle = Paddle((400, 0))

ball = Ball()
scoreboard = Scoreboard()

wall = Turtle()
wall.color("white")
wall.hideturtle()
wall.penup()
wall.goto(0, 300)
wall.setheading(270)

for _ in range(600):
    wall.pendown()
    wall.forward(10)
    wall.penup()
    wall.forward(10)

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeyrelease(right_paddle.stop, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeyrelease(right_paddle.stop, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeyrelease(left_paddle.stop, "w")
screen.onkeypress(left_paddle.down, "s")
screen.onkeyrelease(left_paddle.stop, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    if ball.distance(left_paddle) < 40 and ball.xcor() < -385 or ball.distance(right_paddle) < 40 and ball.xcor() > 385:
        ball.bounce_x()

    if ball.xcor() > 430:
        ball.reset()
        scoreboard.left_point()

    if ball.xcor() < -430:
        ball.reset()
        scoreboard.right_point()

screen.exitonclick()
