from turtle import Turtle


class Middle(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed(0)
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.create_line()

    def create_line(self):
        for i in range(60):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
