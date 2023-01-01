from turtle import Turtle

GAME_END_SCORE = 10


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pen()
        self.setposition(0, 200)
        self.color("white")
        self.player1_score = 0
        self.player2_score = 0
        self.winner = None
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.player1_score} {self.player2_score}",
                   align="center",
                   font=("Courier", 60, "bold"))

    def increase_score(self, player):
        if player == "player1":
            self.player1_score += 1
        elif player == "player2":
            self.player2_score += 1
        self.update_score()

        # Check for winner
        if self.player1_score == GAME_END_SCORE:
            self.winner = "Player 1"
            self.game_over()
        elif self.player2_score == GAME_END_SCORE:
            self.winner = "Player 2"
            self.game_over()

    def game_over(self):
        self.setposition(x=0, y=0)
        self.write("GAME OVER",
                   align="center",
                   font=('Courier', 24, 'bold'))
        self.setposition(x=0, y=-40)
        self.write(f"{self.winner} Wins!",
                   align="center",
                   font=('Courier', 20, 'bold'))
