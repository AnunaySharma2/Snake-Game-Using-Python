from turtle import Turtle

FONT = ("Arial", 22, "normal")
ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.update_scoreboard()

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.penup()
        self.clear()
        self.goto(0, 250)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)
