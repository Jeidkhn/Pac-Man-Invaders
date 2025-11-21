import pygame
from ChargementImages import charger_image

class Bullet:

    def __init__(self, x, y, direction, color, dimension, screen, speed):
        self.position = pygame.Vector2(x, y)
        self.direction = direction
        self.color = color
        self.dimension = dimension
        self.screen = screen
        self.speed = speed
        self.image = charger_image("tir_" + color + ".png")

    def move(self):
        if self.direction == "up":
            self.position.y -= self.speed
        if self.direction == "down":
            self.position.y += self.speed

    def draw(self):
        rectangle= self.image.get_rect(center=(int(self.position.x), int(self.position.y)))
        self.screen.blit(self.image, rectangle)

        # pygame.draw.rect(self.screen, self.color, (self.position, self.dimension))
