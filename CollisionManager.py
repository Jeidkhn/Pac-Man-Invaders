class CollisionManager:
    pass


def is_player_touched(player, bulletManager):
    for bullet in bulletManager.ghost_bullets:
        if (player.position.x - player.width <= bullet.position.x <= player.position.x + player.width
                and player.position.y - player.width <= bullet.position.y <= player.position.y + player.width):
            return True
    return False

