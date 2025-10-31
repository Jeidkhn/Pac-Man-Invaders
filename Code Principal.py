import pygame                                                       # Imports
import Player
import Ghost
import BulletManager
import Score
import CollisionManager
pygame.init()
screen_height = 720
screen_width = 960
screen = pygame.display.set_mode((screen_width, screen_height))    # Taille d'écran rétro
clock = pygame.time.Clock()     # Le temps du jeu
dt = 0.0                                          # Variables
timer = 0.0
interval = 3.0                                    # Intervalle de temps en secondes
running = True

bullet_manager = BulletManager.BulletManager(screen)

ghost1 = Ghost.Ghost(130, 100, "right", "deeppink", (50, 60), screen,           # Objets
                     2, pygame.Vector2(130, 100), pygame.Vector2(130, 290), pygame.Vector2(780, 290),
                     pygame.Vector2(780, 100), bullet_manager)
ghost2 = Ghost.Ghost(550, 100, "right", "red", (50, 60), screen,
                     2, pygame.Vector2(130, 100), pygame.Vector2(130, 290), pygame.Vector2(780, 290),
                     pygame.Vector2(780, 100), bullet_manager)
ghost3 = Ghost.Ghost(780, 290, "left", "deepskyblue", (50, 60), screen,
                     2, pygame.Vector2(130, 100), pygame.Vector2(130, 290), pygame.Vector2(780, 290),
                     pygame.Vector2(780, 100), bullet_manager)
ghost4 = Ghost.Ghost(360, 290, "left", "orange", (50, 60), screen,
                     2, pygame.Vector2(130, 100), pygame.Vector2(130, 290), pygame.Vector2(780, 290),
                     pygame.Vector2(780, 100), bullet_manager)
player = Player.Player(480, 655, "yellow", 40, screen, 9, bullet_manager)
score = Score.Score(screen, 30, 30, pygame.font.SysFont(None, 50), 0, "")


while running == True:                   # Tant que le jeu tourne, la variable est vrai

    for event in pygame.event.get():
        if event.type == pygame.QUIT:    # Si l'écran d'affichage est supprimé, arrêt du jeu, car variable devient fausse
            running = False

    screen.fill("darkblue")

    keys = pygame.key.get_pressed()                                     # Déplacement du joueur
    if keys[pygame.K_w]:
        player.shoot()

    if keys[pygame.K_a]:
        player.move_left()

    if keys[pygame.K_d]:
        player.move_right()

    if timer >= interval:
        ghost1.shoot()
        ghost2.shoot()
        ghost3.shoot()
        ghost4.shoot()
        timer = 0.0

    ghost1.draw()                                                       # Dessins des objets
    ghost2.draw()
    ghost3.draw()
    ghost4.draw()
    player.draw()
    score.show_score()

    ghost1.move()                                                       # Déplacements des fantômes
    ghost2.move()
    ghost3.move()
    ghost4.move()

    bullet_manager.move_and_draw_ghost_bullet()                         # Création des nouveaux tirs
    bullet_manager.move_and_draw_player_bullet()

    if CollisionManager.is_player_touched(player, bullet_manager):      # Collision des tirs
        running = False
    if CollisionManager.is_ghost_touched(ghost1, bullet_manager):
        score.add_score()
        bullet_manager.delete_player_bullet(bullet)

    for bullet in bullet_manager.player_bullets:
        for ghost in [ghost1, ghost2, ghost3, ghost4]:
            if (ghost.position.x <= bullet.position.x <= ghost.position.x + ghost.dimension[0]
            and ghost.position.y <= bullet.position.y <= ghost.position.y + ghost.dimension[1]):
                score.add_score()

    for bullet in bullet_manager.player_bullets:                                         # Suppression tirs hors-écran
        if bullet.position.y <= 0:
            bullet_manager.player_bullets.remove(bullet)

    for bullet in bullet_manager.ghost_bullets:
        if bullet.position.y >= screen_height:
            bullet_manager.ghost_bullets.remove(bullet)

    pygame.display.flip()               # Rafraîchissement de l'image
    timer += dt
    dt = clock.tick(60) / 1000          # Vitesse de rafraîchissement

pygame.quit()