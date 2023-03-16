import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from middle_line import Middle

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
# screen.addshape("table.gif")
# screen.bgpic("table.gif")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
middle = Middle()

screen.listen()
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision With Wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision  with paddle.
    if ball.distance(l_paddle) < 50 and ball.xcor() > 320 or ball.distance(r_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect Collision with right Wall.
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # # Detect collision with Left wall.
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
