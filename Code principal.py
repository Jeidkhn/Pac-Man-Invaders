import pygame

pygame.init()
screen = pygame.display.set_mode((960, 720))    # Taille d'écran rétro
clock = pygame.time.Clock()     # Le temps
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.1)
player_width = 40
bullet_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.1)
bullet_width = 5
bullet_is_moving = False


while running == True:  # Tant que le jeu tourne, la variable est vrai

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Si l'écran d'affichage est supprimé, arrêt du jeu, car variable devient fausse
            running = False

    screen.fill("blue")
    pygame.draw.circle(screen, "yellow", player_pos, player_width)      # Dessin du joueur
    pygame.draw.circle(screen, "red", bullet_pos, bullet_width)      # Dessin du tir

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

    player_pos.x = max(player_width, min(960 - player_width, player_pos.x))   # Limite de déplacement du joueur en x
    bullet_pos.x = max(player_width, min(960 - player_width, bullet_pos.x))    # Limite de déplacement du tir en x
    pygame.display.flip()       # Rafraîchissement de l'image

    dt = clock.tick(60) / 1000      # Vitesse de rafraîchissement

pygame.quit()