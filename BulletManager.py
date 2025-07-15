import pygame
import Bullet


class BulletManager:
    def __init__(self, screen):
        self.screen = screen
        self.player_bullets = []
        self.ghost_bullets = []

    def add_new_player_bullet(self, player):
        player_bullet = Bullet.Bullet(player.position.x, player.position.y, "up", "red", (10, 10), self.screen, 2)
        self.player_bullets.append(player_bullet)
        print("Tir ajouté")

    def move_and_draw_player_bullets(self):
        for i in range(0, len(self.player_bullets)):
            self.player_bullets[i].move()
            self.player_bullets[i].draw()

