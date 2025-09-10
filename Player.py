import pygame
class Player:
    def __init__(self, x, y, color, width, screen, speed, bullet_Manager):
        self.position = pygame.Vector2(x, y)
        self.width = 40
        self.color = color
        self.screen = screen
        self.speed_move = 9
        self.bullet_Manager = bullet_Manager

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.width)

    def move_left(self):
        self.position.x -= self.speed_move
        self.position.x = max(self.width, self.position.x)

    def move_right(self):
        self.position.x += self.speed_move
        self.position.x = min(self.position.x , 960 - self.width)

    def shoot(self):
        self.bullet_Manager.add_new_player_bullet(self)