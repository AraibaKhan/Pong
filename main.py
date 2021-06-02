from turtle import Turtle, Screen
from padle import Padle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# pen = Turtle()
# pen.hideturtle()
# pen.setheading(90)
# pen.goto(0, -300)
# pen.speed("fastest")
# line = True
# while line:
#     pen.penup()
#     pen.forward(20)
#     pen.color("white")
#     pen.pendown()
#     pen.forward(20)
#     if pen.ycor() >= 300:
#         line = False


r_paddle = Padle((350, 0))
l_paddle = Padle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()
scoreboard = Scoreboard()


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.if_coll_wall()
    # detect collision with paddle
    if (ball.xcor() > 330 and ball.distance(r_paddle)< 50) or (ball.xcor() <= -330 and ball.distance(l_paddle) < 50):
        ball.if_coll_padle()
    # detect paddle missing ball
    # if left misses
    if ball.xcor() < -400:
        ball.if_miss_ball()
        scoreboard.right_score()
    # if right misses
    elif ball.xcor() > 400:
        ball.if_miss_ball()
        scoreboard.left_score()



screen.exitonclick()
