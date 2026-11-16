from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.read_high_score()
        self.update_scoreboard()

    def read_high_score(self):
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

    def update_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                    move=False,
                    align=ALIGNMENT,
                    font=FONT)