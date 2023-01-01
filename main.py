from paddle import Paddle
from turtle import Screen

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PONG")
screen.tracer(0)
screen.listen()

# Initialize player 1's paddle
paddle1 = Paddle(start_x=-360, start_y=0)
paddle1.speed("fastest")
screen.onkey(paddle1.move_up, "w")
screen.onkey(paddle1.move_down, "s")

# Initialize layer 2's paddle
paddle2 = Paddle(start_x=350, start_y=0)
paddle2.speed("fastest")
screen.onkey(paddle2.move_up, "Up")
screen.onkey(paddle2.move_down, "Down")

game_running = True
while game_running:
    screen.update()

screen.exitonclick()
