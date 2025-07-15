import pygame
class Bullet:
    def __init__(self, x, y, direction, color, dimension, screen, speed):
        self.position = pygame.Vector2(x, y)
        self.direction = direction
        self.color = color
        self.dimension = (10, 10)
        self.screen = screen
        self.speed = speed

    def move(self):
        if self.direction == "up":
            self.position.y -= self.speed
        if self.direction == "down":
            self.position.y += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.position, self.dimension))