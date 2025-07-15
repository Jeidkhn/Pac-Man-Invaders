import pygame
class Ghost:
    def __init__(self, x, y, direction, color, dimension, screen, speed, top_left, bottom_left, bottom_right, top_right):
        self.position = pygame.Vector2(x, y)
        self.direction = direction
        self.dimension = (50, 60)
        self.color = color
        self.screen = screen
        self.speed = 2
        self.top_left = pygame.Vector2(130, 100)
        self.bottom_left = pygame.Vector2(130, 290)
        self.bottom_right = pygame.Vector2(780, 290)
        self.top_right = pygame.Vector2(780, 100)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.position, self.dimension))
    def move(self):
        if self.direction == "right":                # Déplacement en boucle des fantômes dans le sens horaire
            self.position.x += self.speed
        if self.direction == "down":
            self.position.y += self.speed
        if self.direction == "left":
            self.position.x -= self.speed
        if self.direction == "up":
            self.position.y -= self.speed

        if self.position.x >= self.top_right.x and self.direction == "right":
            self.direction = "down"
        if self.position.y >= self.bottom_right.y and self.direction == "down":
            self.direction = "left"
        if self.position.x <= self.bottom_left.x and self.direction == "left":
            self.direction = "up"
        if self.position.y <= self.top_left.y and self.direction == "up":
            self.direction = "right"
