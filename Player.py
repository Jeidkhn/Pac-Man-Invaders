import pygame
class Player:
    def __init__(self, x, y, color, width, screen, speed, bulletManager):
        self.position = pygame.Vector2(x, y)
        self.width = 40
        self.color = color
        self.screen = screen
        self.speed_move = 9
        self.bulletManager = bulletManager

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.width)

    def move_left(self):
        self.position.x -= self.speed_move
        self.position.x = min(960 - self.width, self.position.x)

    def move_right(self):
        self.position.x += self.speed_move
        self.position.x = max(self.width, self.position.x)

    def shoot(self):
        self.bulletManager.addNewPlayerBullet(self)