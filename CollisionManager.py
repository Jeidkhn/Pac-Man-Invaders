import pygame
import BulletManager
import Player
class CollisionManager:

    def is_player_touched(player, bulletManager):
        for bullet in bullet_manager.ghost_bullets:
            if (player.position.x - player.width <= bullet.position.x <= player.position.x + player.width
                    and player.position.y - player.width <= bullet.position.y <= player.position.y + player.width):
                print(score.score)
                running = False

