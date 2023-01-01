from ball import Ball
from paddle import Paddle
from turtle import Screen
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PONG")
screen.tracer(0)
screen.listen()

# Initialize Player 1's paddle
paddle1 = Paddle(start_x=-360, start_y=0)
paddle1.speed("fastest")
screen.onkey(paddle1.move_up, "w")
screen.onkey(paddle1.move_down, "s")

# Initialize Player 2's paddle
paddle2 = Paddle(start_x=350, start_y=0)
paddle2.speed("fastest")
screen.onkey(paddle2.move_up, "Up")
screen.onkey(paddle2.move_down, "Down")

# Initialize ball
ball = Ball()

game_running = True
while game_running:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.xcor() < -330 and ball.distance(paddle1) < 50 or \
            ball.xcor() > 320 and ball.distance(paddle2) < 50:
        ball.bounce_x()

    # Detect goal scored
    if ball.xcor() > 320 and ball.distance(paddle2) > 50:
        # Player 1 scores
        pass
    elif ball.xcor() < -330 and ball.distance(paddle1) > 50:
        # Player 2 scores
        pass

    # Reset ball
    if ball.xcor() > 370 or ball.xcor() < -380:
        ball.new_ball()

screen.exitonclick()
