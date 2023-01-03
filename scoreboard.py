from turtle import Turtle
FONT = ("Courier", 24, "bold")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.pu()
        self.color("black")
        self.goto(-220, 260)
        self.show_level()

    def show_level(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)


    def update_level(self):
        self.level += 1



    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
