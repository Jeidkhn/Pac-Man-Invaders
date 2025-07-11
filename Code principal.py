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
player_pos = pygame.Vector2(480, 655)
bullet_pos = pygame.Vector2(480, 655)
top_left_pos = pygame.Vector2(130, 100)
bottom_left_pos = pygame.Vector2(130, 290)
bottom_right_pos = pygame.Vector2(780, 290)
top_right_pos = pygame.Vector2(780, 100)
ghost_area = pygame.Vector2(130, 100)         # Temporaire !
ghost_dimension = 50, 60
player_width = 40
bullet_width = 5
bullet_is_moving = False
ghost1_direction = "right"
ghost2_direction = "right"
ghost3_direction = "left"
ghost4_direction = "left"
score = 0
font_dimension = 50
font = pygame.font.SysFont(None, font_dimension)
ghosts_pos = [ghost1_pos, ghost2_pos, ghost3_pos, ghost4_pos]
ghosts_direction = [ghost1_direction, ghost2_direction, ghost3_direction, ghost4_direction]

while running == True:  # Tant que le jeu tourne, la variable est vrai

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Si l'écran d'affichage est supprimé, arrêt du jeu, car variable devient fausse
            running = False

    screen.fill("blue")
    pygame.draw.rect(screen, "black", (*ghost_area, 700, 250))      # Temporaire !
    pygame.draw.rect(screen, "deeppink", (*ghost1_pos, *ghost_dimension))       # Dessins des fantômes
    pygame.draw.rect(screen, "red", (*ghost2_pos, *ghost_dimension))
    pygame.draw.rect(screen, "deepskyblue", (*ghost3_pos, *ghost_dimension))
    pygame.draw.rect(screen, "orange", (*ghost4_pos, *ghost_dimension))
    pygame.draw.circle(screen, "yellow", player_pos, player_width)      # Dessin du joueur
    pygame.draw.circle(screen, "purple", bullet_pos, bullet_width)      # Dessin du tir

    score_text = font.render(f"SCORE: {score}", True, ("black"))        # Dessin du score
    screen.blit(score_text, (30, 30))

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

    for pos in ghosts_pos:                                      # Parmi la liste de positions des fantômes
        if (pos.x <= bullet_pos.x <= pos.x + 50 and             # Collisions entres les fantômes et le tir
                pos.y <= bullet_pos.y <= pos.y + 60):
            bullet_pos = player_pos.copy()
            bullet_is_moving = False
            score += 5

    for i in range(0, len(ghosts_pos)):         # Parmi la liste de positions et directions des fantômes
        pos = ghosts_pos[i]
        direction = ghosts_direction[i]
        if direction == "right":                # Déplacement en boucles des fantômes dans le sens horaire
            pos.y = top_left_pos.y
            pos.x += 3
        if direction == "down":
            pos.x = top_right_pos.x
            pos.y += 3
        if direction == "left":
            pos.y = bottom_right_pos.y
            pos.x -= 3
        if direction == "up":
            pos.x = bottom_left_pos.x
            pos.y -= 3

        if pos.x >= top_right_pos.x and direction == "right":
            direction = "down"
        if pos.y >= bottom_right_pos.y and direction == "down":
            direction = "left"
        if pos.x <= bottom_left_pos.x and direction == "left":
            direction = "up"
        if pos.y <= top_left_pos.y and direction == "up":
            direction = "right"

        ghosts_direction[i] = direction


    pygame.display.flip()       # Rafraîchissement de l'imagse

    dt = clock.tick(60) / 1000       # Vitesse de rafraîchissement

pygame.quit()