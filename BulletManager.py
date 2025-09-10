import Bullet
class BulletManager:
    def __init__(self, screen):
        self.screen = screen
        self.player_bullets = []
        self.ghost_bullets = []

    def add_new_player_bullet(self, player):
        player_bullet = Bullet.Bullet(player.position.x - 5, player.position.y - 5, "up", "red", (10, 10), self.screen, 12)
        self.player_bullets.append(player_bullet)

    def move_and_draw_player_bullets(self):
        for i in range(0, len(self.player_bullets)):
            self.player_bullets[i].move()
            self.player_bullets[i].draw()

    def add_new_ghost_bullet(self, ghost):
        bullet_ghost = Bullet.Bullet(ghost.position.x - 5, ghost.position.y - 5, "down", "deeppink", (10, 10), self.screen, 7)
        self.ghost_bullets.append(bullet_ghost)

    def move_and_draw_ghost_bullets(self):
        for i in range(0, len(self.ghost_bullets)):
            self.ghost_bullets[i].move()
            self.ghost_bullets[i].draw()


