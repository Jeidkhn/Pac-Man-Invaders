class CollisionManager:
    pass

def is_player_touched(player, bulletManager):
    for bullet in bulletManager.ghost_bullets:
        if (player.position.x - player.width <= bullet.position.x <= player.position.x + player.width
                and player.position.y - player.width <= bullet.position.y <= player.position.y + player.width):
            return True
    return False

def is_ghost_touched(ghost, bulletManager):
    for bullet in bulletManager.player_bullets:
        if (ghost.position.x <= bullet.position.x <= ghost.position.x + ghost.dimension[0]
                and ghost.position.y <= bullet.position.y <= ghost.position.y + ghost.dimension[1]):
            return bullet
    return None

def is_bonus_touched(bonus, bulletManager):
    for bullet in bulletManager.player_bullets:
        if (bonus.position.x <= bullet.position.x <= bonus.position.x + bonus.dimension[0]
                and bonus.position.y <= bullet.position.y <= bonus.position.y + bonus.dimension[1]):
            return bullet
    return None