import pygame
class Score:
    def __init__(self, screen):
        self.screen = screen

    def show_score(self):
        self.score_text = font.render(f"SCORE: {score}", True, ("black"))                     # Affichage du score
        self.screen.blit(score_text, (30, 30))