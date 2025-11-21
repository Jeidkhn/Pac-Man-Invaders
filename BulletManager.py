import Bullet
class BulletManager:

    def __init__(self, screen):
        self.screen = screen
        self.player_bullets = []
        self.ghost_bullets = []

    def add_new_player_bullet(self, player):
        player_bullet = Bullet.Bullet(player.position.x - 5, player.position.y - 5, "up",
                                      "vert", (10, 10), self.screen, 12)
        self.player_bullets.append(player_bullet)

    def move_and_draw_player_bullet(self):
        for i in range(0, len(self.player_bullets)):
            self.player_bullets[i].move()
            self.player_bullets[i].draw()

    def add_new_ghost_bullet(self, ghost):
        ghost_bullet = Bullet.Bullet(ghost.position.x + 20, ghost.position.y + 25, "down",
                                     "rouge", (10, 10), self.screen, 7)
        self.ghost_bullets.append(ghost_bullet)

    def move_and_draw_ghost_bullet(self):
        for i in range(0, len(self.ghost_bullets)):
            self.ghost_bullets[i].move()
            self.ghost_bullets[i].draw()

    def delete_player_bullet(self, bullet):
        self.player_bullets.remove(bullet)

    def delete_ghost_bullet(self, bullet):
        self.ghost_bullets.remove(bullet)


