import pygame
from random import randint
from ChargementImages import charger_image

class Bonus:

    def __init__(
            self,
            x,
            y,
            color,
            dimension,
            screen,
            speed,
            limit_left,
            limit_right,
            counter,
    ):
        self.position = pygame.Vector2(x, y)
        self.direction = randint(0,1)
        self.dimension = dimension
        self.color = color
        self.screen = screen
        self.speed = speed
        self.limit_left = limit_left
        self.limit_right = limit_right
        self.counter = counter
        self.image = charger_image("bonus.png")

    def draw(self):
        rectangle= self.image.get_rect(center=(int(self.position.x), int(self.position.y)))
        self.screen.blit(self.image, rectangle)

    def move(self):
        if self.direction == 0:
            self.position.x -= self.speed
        if self.direction == 1:
            self.position.x += self.speed

        if self.position.x >= self.limit_right.x and self.direction == 1:
            self.direction = 0
        if self.position.x <= self.limit_left.x and self.direction == 0:
            self.direction = 1


    def change_speed(self, speed):
        if self.direction == "left":
            self.speed = speed
        else:
            self.speed = speed




