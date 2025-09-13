class Score:

    def __init__(self, screen, x, y, font, score, text):
        self.screen = screen
        self.position = x, y
        self.font = font
        self.score = score
        self.text = text

    def show_score(self):
        text = self.font.render(f"SCORE: {self.score}", True, "black")
        self.screen.blit(text, self.position)