class Score:

    def __init__(self, screen, x, y, font, score, text):
        self.screen = screen
        self.position = x, y
        self.font = font
        self.score = score
        self.text = text

    def show_score(self):
        text = self.font.render(f"SCORE: {self.score}", True, "White")
        self.screen.blit(text, self.position)

    def add_score_normal(self):
        self.score += 10

    def add_score_bonus(self):
        self.score += 150