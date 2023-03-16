from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.create_paddle(positions)

    def create_paddle(self, coordinate):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coordinate)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(y=new_y, x=self.xcor())

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(y=new_y, x=self.xcor())
