import pygame

pygame.init()
screen = pygame.display.set_mode((960, 720))    # Taille d'écran rétro
clock = pygame.time.Clock()     # Le temps du jeu
dt = 0                                          # Variables
timer = 0
interval = 3.0                                    # Intervalle de temps en secondes
running = True
bullet_player_is_moving = False
bullet_ghost_is_moving = False
ghost1_pos = pygame.Vector2(130, 100)                # Positions
ghost2_pos = pygame.Vector2(550, 100)
ghost3_pos = pygame.Vector2(780, 290)
ghost4_pos = pygame.Vector2(360, 290)
bullet_ghost1_pos = pygame.Vector2(150, 125)
bullet_ghost2_pos = pygame.Vector2(570, 125)
bullet_ghost3_pos = pygame.Vector2(800, 315)
bullet_ghost4_pos = pygame.Vector2(380, 315)
player_pos = pygame.Vector2(480, 655)
bullet_player_pos = pygame.Vector2(475, 650)
ghost_top_left_pos = pygame.Vector2(130, 100)
ghost_bottom_left_pos = pygame.Vector2(130, 290)
ghost_bottom_right_pos = pygame.Vector2(780, 290)
ghost_top_right_pos = pygame.Vector2(780, 100)
bullet_top_left_pos = pygame.Vector2(150, 125)
bullet_bottom_left_pos = pygame.Vector2(150, 315)
bullet_bottom_right_pos = pygame.Vector2(800, 315)
bullet_top_right_pos = pygame.Vector2(800, 125)
ghost_area = pygame.Vector2(130, 100)                # Temporaire !
ghost_dimension = 50, 60                             # Dimensions
player_width = 40
bullet_dimension = 10, 10
ghost1_direction = "right"
ghost2_direction = "right"
ghost3_direction = "left"
ghost4_direction = "left"
bullet_ghost1_direction = "right"
bullet_ghost2_direction = "right"
bullet_ghost3_direction = "left"
bullet_ghost4_direction = "left"
speed = 3
score = 0
font_dimension = 50
font = pygame.font.SysFont(None, font_dimension)
ghosts_pos = [ghost1_pos, ghost2_pos, ghost3_pos, ghost4_pos]                                   # Listes
ghosts_direction = [ghost1_direction, ghost2_direction, ghost3_direction, ghost4_direction]
bullet_ghosts_pos = [bullet_ghost1_pos, bullet_ghost2_pos, bullet_ghost3_pos, bullet_ghost4_pos]
bullet_ghosts_direction = [ghost1_direction, ghost2_direction, ghost3_direction, ghost4_direction]

while running == True:  # Tant que le jeu tourne, la variable est vrai

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Si l'écran d'affichage est supprimé, arrêt du jeu, car variable devient fausse
            running = False

    screen.fill("blue")
    pygame.draw.rect(screen, "white", (*ghost_area, 700, 250))                       # Temporaire !
    pygame.draw.rect(screen, "black", (*ghost1_pos, *ghost_dimension))            # Dessins des ennemis
    pygame.draw.rect(screen, "black", (*ghost2_pos, *ghost_dimension))
    pygame.draw.rect(screen, "black", (*ghost3_pos, *ghost_dimension))
    pygame.draw.rect(screen, "black", (*ghost4_pos, *ghost_dimension))
    pygame.draw.rect(screen, "deeppink", (*bullet_ghost1_pos, *bullet_dimension))    # Dessins des tirs ennemis
    pygame.draw.rect(screen, "red", (*bullet_ghost2_pos, *bullet_dimension))
    pygame.draw.rect(screen, "deepskyblue", (*bullet_ghost3_pos, *bullet_dimension))
    pygame.draw.rect(screen, "orange", (*bullet_ghost4_pos, *bullet_dimension))
    pygame.draw.circle(screen, "yellow", player_pos, player_width)                   # Dessin du joueur
    pygame.draw.rect(screen, "yellow", (*bullet_player_pos, *bullet_dimension))      # Dessin du tir joueur

    score_text = font.render(f"SCORE: {score}", True, ("black"))                     # Affichage du score
    screen.blit(score_text, (30, 30))

    if bullet_player_is_moving == True:    # Si la variable de déplacement du tir joueur est vrai, le tir monte
        bullet_player_pos.y -= 800 * dt

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        bullet_player_is_moving = True     # Si "w" est pressé, la variable de déplacement du tir joueur devient vrai
    if keys[pygame.K_a]:
        player_pos.x -= 600 * dt
        if bullet_player_is_moving == False:
            bullet_player_pos.x -= 600 * dt
    if keys[pygame.K_d]:
        player_pos.x += 600 * dt
        if bullet_player_is_moving == False:
            bullet_player_pos.x += 600 * dt

    if bullet_player_pos.y <= 0:       # Si le tir joueur dépasse l'écran en y, il revient à la position du joueur
        bullet_player_pos.x = player_pos.x - 5
        bullet_player_pos.y = player_pos.y - 5
        bullet_player_is_moving = False

    player_pos.x = max(player_width, min(960 - player_width, player_pos.x))   # Limite de déplacement du joueur en x
    bullet_player_pos.x = max(player_width, min(960 - player_width, bullet_player_pos.x))    # Limite de déplacement du tir en x

    for pos in ghosts_pos:                                      # Parmi la liste de positions des ennemis
        if (pos.x <= bullet_player_pos.x <= pos.x + 50 and             # Collisions entre les ennemis et le tir joueur
                pos.y <= bullet_player_pos.y <= pos.y + 60):
            bullet_player_pos.x = player_pos.x - 5
            bullet_player_pos.y = player_pos.y - 5
            bullet_player_is_moving = False
            score += 5

    for index in range(0, len(ghosts_pos)):         # Parmi la liste de positions et de directions des ennemis
        pos = ghosts_pos[index]
        direction = ghosts_direction[index]
        if direction == "right":                # Déplacement en boucle des fantômes dans le sens horaire
            pos.x += 2
        if direction == "down":
            pos.y += 2
        if direction == "left":
            pos.x -= 2
        if direction == "up":
            pos.y -= 2

        if pos.x >= ghost_top_right_pos.x and direction == "right":
            direction = "down"
        if pos.y >= ghost_bottom_right_pos.y and direction == "down":
            direction = "left"
        if pos.x <= ghost_bottom_left_pos.x and direction == "left":
            direction = "up"
        if pos.y <= ghost_top_left_pos.y and direction == "up":
            direction = "right"

        ghosts_direction[index] = direction


    # for i in range(0, len(bullet_ghosts_pos)):          # Parmi la liste de position et de direction des tirs ennemis
    #     pos = bullet_ghosts_pos[i]
    #     direction = bullet_ghosts_direction[i]

    #
    #     if direction == "right":                 # Déplacement en boucle des tirs ennemis dans le sens horaire
    #         pos.x += 2
    #     if direction == "down":
    #         pos.y += 2
    #     if direction == "left":
    #         pos.x -= 2
    #     if direction == "up":
    #         pos.y -= 2

        if pos.x >= bullet_top_right_pos.x and direction == "right":
            direction = "down"
        if pos.y >= bullet_bottom_right_pos.y and direction == "down":
            direction = "left"
        if pos.x <= bullet_bottom_left_pos.x and direction == "left":
            direction = "up"
        if pos.y <= bullet_top_left_pos.y and direction == "up":
            direction = "right"

        bullet_ghosts_direction[index] = direction


    if bullet_ghost_is_moving == True:
        bullet_ghost1_pos.y += 3
        bullet_ghost1_pos.x += 0
        bullet_ghost1_direction = False

    if bullet_ghost1_pos.y >= 720:                   # Si le tir ennemi dépasse l'écran en y, il revient à la position du fantôme
        #bullet_ghost1_pos.x = ghost1_pos.x + 20
        #bullet_ghost1_pos.y = ghost1_pos.y + 25
        bullet_ghost1_direction = ghost1_direction
        bullet_ghost_is_moving = False



    for pos in bullet_ghosts_pos:                             # Parmi la liste de positions des tirs ennemis
        if (pos.x - 40 <= player_pos.x <= pos.x + 40 and      # Collisions entre les tirs ennemis et le joueur, défaite
                pos.y - 40 <= player_pos.y <= pos.y + 40):
                running = False


    pygame.display.flip()       # Rafraîchissement de l'imagse
    timer += dt
    dt = clock.tick(60) / 1000       # Vitesse de rafraîchissement

pygame.quit()