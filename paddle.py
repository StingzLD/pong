from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_x, start_y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(x=start_x, y=start_y)
        self.color("white")

    def move_up(self):
        self.setposition(x=self.xcor(), y=self.ycor() + 20)

    def move_down(self):
        self.setposition(x=self.xcor(), y=self.ycor() - 20)
