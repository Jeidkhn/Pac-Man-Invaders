import pygame

pygame.init()
screen = pygame.display.set_mode((960, 720))    # Taille d'écran rétro
clock = pygame.time.Clock()     # Le temps
running = True
dt = 0
ghost1_pos = pygame.Vector2(130, 100)       # Les positions
ghost2_pos = pygame.Vector2(550, 100)
ghost3_pos = pygame.Vector2(780, 290)
ghost4_pos = pygame.Vector2(360, 290)
player_pos = pygame.Vector2(960 / 2, 655)
ghost_dimension = 50, 60
ghost_area = pygame.Vector2(130, 100)         # Temporaire !
player_width = 40
bullet_pos = pygame.Vector2(960 / 2, 655)
bullet_width = 5
bullet_is_moving = False
top_left_pos = pygame.Vector2(130, 100)
bottom_left_pos = pygame.Vector2(130, 290)
bottom_right_pos = pygame.Vector2(780, 290)
top_right_pos = pygame.Vector2(780, 100)
ghost1_direction = "right"
ghost2_direction = "right"
ghost3_direction = "left"
ghost4_direction = "left"

while running == True:  # Tant que le jeu tourne, la variable est vrai

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Si l'écran d'affichage est supprimé, arrêt du jeu, car variable devient fausse
            running = False

    screen.fill("blue")
    pygame.draw.rect(screen, "black", (*ghost_area, 700, 250))      # Temporaire !
    pygame.draw.rect(screen, "deeppink", (*ghost1_pos, *ghost_dimension))       # Dessins des ennemis
    pygame.draw.rect(screen, "red", (*ghost2_pos, *ghost_dimension))
    pygame.draw.rect(screen, "deepskyblue", (*ghost3_pos, *ghost_dimension))
    pygame.draw.rect(screen, "orange", (*ghost4_pos, *ghost_dimension))
    pygame.draw.circle(screen, "yellow", player_pos, player_width)      # Dessin du joueur
    pygame.draw.circle(screen, "purple", bullet_pos, bullet_width)      # Dessin du tir

    if bullet_is_moving == True:    # Si la variable de déplacement du tir est vrai, le tir monte
        bullet_pos.y -= 800 * dt

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        bullet_is_moving = True     # Si "w" est pressé, la variable de déplacement du tir devient vrai
    if keys[pygame.K_a]:
        player_pos.x -= 600 * dt
        if bullet_is_moving == False:
            bullet_pos.x -= 600 * dt
    if keys[pygame.K_d]:
        player_pos.x += 600 * dt
        if bullet_is_moving == False:
            bullet_pos.x += 600 * dt

    if bullet_pos.y <= 0:       # Si le tir dépasse l'écran en y, le tir revient à la position du joueur
        bullet_pos = player_pos.copy()
        bullet_is_moving = False

    player_pos.x = max(player_width, min(960 - player_width, player_pos.x))   # Limite de déplacement du joueur en x
    bullet_pos.x = max(player_width, min(960 - player_width, bullet_pos.x))    # Limite de déplacement du tir en x

    if (ghost1_pos.x <= bullet_pos.x <= ghost1_pos.x + 50 and       # Collision entre le 1er fantôme et le tir
    ghost1_pos.y <= bullet_pos.y <= ghost1_pos.y + 60):
        bullet_pos = player_pos.copy()
        bullet_is_moving = False

    if (ghost2_pos.x <= bullet_pos.x <= ghost2_pos.x + 50 and       # Collision entre le 2ème fantôme et le tir
            ghost2_pos.y <= bullet_pos.y <= ghost2_pos.y + 60):
        bullet_pos = player_pos.copy()
        bullet_is_moving = False

    if (ghost3_pos.x <= bullet_pos.x <= ghost3_pos.x + 50 and       # Collision entre le 3ème fantôme et le tir
            ghost3_pos.y <= bullet_pos.y <= ghost3_pos.y + 60):
        bullet_pos = player_pos.copy()
        bullet_is_moving = False

    if (ghost4_pos.x <= bullet_pos.x <= ghost4_pos.x + 50 and       # Collision entre le 4ème fantôme et le tira
            ghost4_pos.y <= bullet_pos.y <= ghost4_pos.y + 60):
        bullet_pos = player_pos.copy()
        bullet_is_moving = False

    if ghost1_direction == "right":         # Déplacement en boucle du 1er fantôme
        ghost1_pos.y = top_left_pos.y
        ghost1_pos.x += 3
    if ghost1_direction == "down":
        ghost1_pos.x = top_right_pos.x
        ghost1_pos.y += 3
    if ghost1_direction == "left":
        ghost1_pos.y = bottom_right_pos.y
        ghost1_pos.x -= 3
    if ghost1_direction == "up":
        ghost1_pos.x = bottom_left_pos.x
        ghost1_pos.y -= 3

    if ghost1_pos.x >= top_right_pos.x and ghost1_direction == "right":
        ghost1_direction = "down"
    if ghost1_pos.y >= bottom_right_pos.y and ghost1_direction == "down":
        ghost1_direction = "left"
    if ghost1_pos.x <= bottom_left_pos.x and ghost1_direction == "left":
        ghost1_direction = "up"
    if ghost1_pos.y <= top_left_pos.y and ghost1_direction == "up":
        ghost1_direction = "right"

    if ghost2_direction == "right":         # Déplacement en boucle du 2ème fantôme
        ghost2_pos.y = top_left_pos.y
        ghost2_pos.x += 3
    if ghost2_direction == "down":
        ghost2_pos.x = top_right_pos.x
        ghost2_pos.y += 3
    if ghost2_direction == "left":
        ghost2_pos.y = bottom_right_pos.y
        ghost2_pos.x -= 3
    if ghost2_direction == "up":
        ghost2_pos.x = bottom_left_pos.x
        ghost2_pos.y -= 3

    if ghost2_pos.x >= top_right_pos.x and ghost2_direction == "right":
        ghost2_direction = "down"
    if ghost2_pos.y >= bottom_right_pos.y and ghost2_direction == "down":
        ghost2_direction = "left"
    if ghost2_pos.x <= bottom_left_pos.x and ghost2_direction == "left":
        ghost2_direction = "up"
    if ghost2_pos.y <= top_left_pos.y and ghost2_direction == "up":
        ghost2_direction = "right"

    if ghost3_direction == "right":         # Déplacement en boucle du 3ème fantôme
        ghost3_pos.y = top_left_pos.y
        ghost3_pos.x += 3
    if ghost3_direction == "down":
        ghost3_pos.x = top_right_pos.x
        ghost3_pos.y += 3
    if ghost3_direction == "left":
        ghost3_pos.y = bottom_right_pos.y
        ghost3_pos.x -= 3
    if ghost3_direction == "up":
        ghost3_pos.x = bottom_left_pos.x
        ghost3_pos.y -= 3

    if ghost3_pos.x >= top_right_pos.x and ghost3_direction == "right":
        ghost3_direction = "down"
    if ghost3_pos.y >= bottom_right_pos.y and ghost3_direction == "down":
        ghost3_direction = "left"
    if ghost3_pos.x <= bottom_left_pos.x and ghost3_direction == "left":
        ghost3_direction = "up"
    if ghost3_pos.y <= top_left_pos.y and ghost3_direction == "up":
        ghost3_direction = "right"

    if ghost4_direction == "right":         # Déplacement en boucle du 4ème fantôme
        ghost4_pos.y = top_left_pos.y
        ghost4_pos.x += 3
    if ghost4_direction == "down":
        ghost4_pos.x = top_right_pos.x
        ghost4_pos.y += 3
    if ghost4_direction == "left":
        ghost4_pos.y = bottom_right_pos.y
        ghost4_pos.x -= 3
    if ghost4_direction == "up":
        ghost4_pos.x = bottom_left_pos.x
        ghost4_pos.y -= 3

    if ghost4_pos.x >= top_right_pos.x and ghost4_direction == "right":
        ghost4_direction = "down"
    if ghost4_pos.y >= bottom_right_pos.y and ghost4_direction == "down":
        ghost4_direction = "left"
    if ghost4_pos.x <= bottom_left_pos.x and ghost4_direction == "left":
        ghost4_direction = "up"
    if ghost4_pos.y <= top_left_pos.y and ghost4_direction == "up":
        ghost4_direction = "right"


    pygame.display.flip()       # Rafraîchissement de l'imagse

    dt = clock.tick(60) / 1000       # Vitesse de rafraîchissement

pygame.quit()