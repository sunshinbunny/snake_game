from turtle import Turtle
ALIGNMENT = "center"
FONT = ("DM Sans", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 250)
        self.score = 0
        with open("data.txt") as self.data:
            self.high_score = int(self.data.read())
        self.color("white")
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as self.data:
                self.data.write(str(self.score))
        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align = ALIGNMENT, font=FONT)

    def change_score(self):
        self.score += 1
        self.update_scoreboard()


