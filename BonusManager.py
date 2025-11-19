import Bonus
import pygame
class BonusManager:

    def __init__(self, screen):
        self.screen = screen
        self.bonus = None

    def add_new_bonus (self, bonus):
        new_bonus = Bonus.Bonus(bonus.position.x, bonus.position.y,
                                     "white", (30, 30), self.screen, 7, pygame.Vector2(190, 200),
                                pygame.Vector2(720, 200),
    0
                                )
        self.bonus = new_bonus

    def move_and_draw_bonus(self):
        if self.bonus:
            self.bonus.move()
            self.bonus.draw()

    def delete_bonus(self):
        print("delete_bonus")
        self.bonus = None
