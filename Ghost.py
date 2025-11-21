import pygame
from ChargementImages import charger_image

class Ghost:

    def __init__(
            self,
            x,
            y,
            direction,
            color,
            dimension,
            screen,
            speed,
            top_left,
            bottom_left,
            bottom_right,
            top_right,
            bullet_Manager,
            counter,
            interval
    ):
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
        self.counter = counter
        self.interval = interval
        self.image = charger_image(color + ".png")
        largeur, hauteur = self.image.get_size()
        self.imageDouble = pygame.transform.smoothscale(self.image, (largeur * 2, hauteur * 2))



    def draw(self):
        rectangle= self.imageDouble.get_rect(center=(int(self.position.x), int(self.position.y)))
        self.screen.blit(self.imageDouble, rectangle)
        self.counter += 1

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
        if self.counter % self.interval == 0:
            self.bullet_Manager.add_new_ghost_bullet(self)

    def change_speed(self, speed):
        self.speed = speed
