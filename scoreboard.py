from turtle import Turtle

FONT = ("Courier", 60, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("green")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=-100, y=200)
        self.write(self.l_score, move=False, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, move=False, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
