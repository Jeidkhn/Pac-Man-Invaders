import pygame
from ChargementImages import charger_image
class Player:

    def __init__(
            self,
            x,
            y,
            color,
            width,
            screen,
            speed,
            bullet_Manager,
            counter,
            interval
    ):
        self.position = pygame.Vector2(x, y)
        self.width = width
        self.color = color
        self.screen = screen
        self.speed_move = speed
        self.bullet_Manager = bullet_Manager
        self.counter = counter
        self.interval = interval
        self.image = charger_image("pacman.png")
        largeur, hauteur = self.image.get_size()
        self.imageDouble = pygame.transform.smoothscale(self.image, (largeur * 2, hauteur * 2))


    def draw(self):
        rectangle= self.imageDouble.get_rect(center=(int(self.position.x), int(self.position.y)))
        self.screen.blit(self.imageDouble, rectangle)
        self.counter += 1

    def move_left(self):
        self.position.x -= self.speed_move
        self.position.x = max(self.width, self.position.x)

    def move_right(self):
        self.position.x += self.speed_move
        self.position.x = min(self.position.x , 960 - self.width)

    def shoot(self):
        if self.counter % self.interval == 0:
            self.bullet_Manager.add_new_player_bullet(self)
