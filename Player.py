import pygame
class Player:

    def __init__(self, x, y, color, width, screen, speed, bullet_Manager, timer, interval):
        self.position = pygame.Vector2(x, y)
        self.width = width
        self.color = color
        self.screen = screen
        self.speed_move = speed
        self.bullet_Manager = bullet_Manager
        self.timer = timer
        self.interval = interval


    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.width)

    def move_left(self):
        self.position.x -= self.speed_move
        self.position.x = max(self.width, self.position.x)

    def move_right(self):
        self.position.x += self.speed_move
        self.position.x = min(self.position.x , 960 - self.width)

    def shoot(self):
        if self.timer >= self.interval:
            self.bullet_Manager.add_new_player_bullet(self)
            self.timer = 0