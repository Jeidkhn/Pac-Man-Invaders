import pygame
class Ghost:

    def __init__(self, x, y, direction, color, dimension, screen, speed, top_left, bottom_left, bottom_right,
                 top_right, bullet_Manager):
        self.position = pygame.Vector2(x, y)
        self.direction = direction
        self.dimension = dimension
        self.color = color
        self.screen = screen
        self.speed = speed
        self.top_left = top_left
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.top_right = top_right
        self.bullet_Manager = bullet_Manager

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.position, self.dimension))
    def move(self):                                 # Déplacement en boucle des fantômes dans le sens horaire
        if self.direction == "right":
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

    def shoot(self):
        self.bullet_Manager.add_new_ghost_bullet(self)
