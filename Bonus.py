import pygame
class Bonus:

    def __init__(
            self,
            x,
            y,
            direction,
            color,
            dimension,
            screen,
            speed,
            limit_left,
            limit_right,
            counter,
            interval
    ):
        self.position = pygame.Vector2(x, y)
        self.direction = direction
        self.dimension = dimension
        self.color = color
        self.screen = screen
        self.speed = speed
        self.limit_left = limit_left
        self.limit_right = limit_right
        self.counter = counter
        self.interval = interval