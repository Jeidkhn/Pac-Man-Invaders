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


while running == True:  # Tant que le jeu tourne, la variable est vrai

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Si l'écran d'affichage est supprimé, arrêt du jeu, car variable devient fausse
            running = False

    screen.fill("blue")
    pygame.draw.rect(screen, "black", (*ghost_area, 700, 250))      # Temporaire !
    pygame.draw.rect(screen, "deeppink", (*ghost1_pos, *ghost_dimension))       # Dessins des ennemis
    pygame.draw.rect(screen, "red", (*ghost2_pos, *ghost_dimension))
    pygame.draw.rect(screen, "deepskyblue", (*ghost3_pos, *ghost_dimension))
    pygame.draw.rect(screen, "yellow", (*ghost4_pos, *ghost_dimension))
    pygame.draw.circle(screen, "yellow", player_pos, player_width)      # Dessin du joueur
    pygame.draw.circle(screen, "purple", bullet_pos, bullet_width)      # Dessin du tir

    if bullet_is_moving == True:    # Si la variable de déplacement du tir est vrai, le tir monte
        bullet_pos.y -= 700 * dt

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
    pygame.display.flip()       # Rafraîchissement de l'imagse

    dt = clock.tick(60) / 1000      # Vitesse de rafraîchissement

pygame.quit()