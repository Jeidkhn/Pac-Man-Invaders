from random import randint

import pygame                                                       # Imports de fichiers
import Player
import Ghost
import BulletManager
import Score
import CollisionManager
import cmath

pygame.init()
screen_height = 720
screen_width = 960
screen = pygame.display.set_mode((screen_width, screen_height))    # Taille d'écran rétro
clock = pygame.time.Clock()     # Le temps du jeu
dt = 0.0                                          # Variables
running = True

bullet_manager = BulletManager.BulletManager(screen)

ghost1 = Ghost.Ghost(
    130,
    100,
    "right",
    "deeppink",
    (50, 60),
    screen,
    3,
    pygame.Vector2(130, 100),
    pygame.Vector2(130, 290),
    pygame.Vector2(780, 290),
    pygame.Vector2(780, 100),
    bullet_manager,
    0,
    600
)

ghost2 = Ghost.Ghost(
    550,
    100,
    "right",
    "red",
    (50, 60),
    screen,
    3,
    pygame.Vector2(130, 100),
    pygame.Vector2(130, 290),
    pygame.Vector2(780, 290),
    pygame.Vector2(780, 100),
    bullet_manager,
    0,
    900
)

ghost3 = Ghost.Ghost(
    780,
    290,
    "left",
    "deepskyblue",
    (50, 60),
    screen,
    3,
    pygame.Vector2(130, 100),
    pygame.Vector2(130, 290),
    pygame.Vector2(780, 290),
    pygame.Vector2(780, 100),
    bullet_manager,
    0,
    750
)

ghost4 = Ghost.Ghost(
    360,
    290,
    "left",
    "orange",
    (50, 60),
    screen,
    3,
    pygame.Vector2(130, 100),
    pygame.Vector2(130, 290),
    pygame.Vector2(780, 290),
    pygame.Vector2(780, 100),
    bullet_manager,
    0,
    450
)

ghost_bonus = Ghost.Ghost(
    360,
    160,
    "left",
    "yellow",
    (40,40),
    screen,
    10,
    pygame.Vector2(130, 160),
    pygame.Vector2(130, 160),
    pygame.Vector2(780, 160),
    pygame.Vector2(780, 160),
    None,
    0,
    99999999
)

player = Player.Player(
    480,
    655,
    "yellow",
    40,
    screen,
    9,
    bullet_manager,
    0,
    15
)

score = Score.Score(
    screen,
    30,
    30,
    pygame.font.SysFont(None, 50), 0, ""
)

Ghosts = [ghost1, ghost2, ghost3, ghost4, ghost_bonus]

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

    for ghost in Ghosts:
        ghost.draw()
        ghost.move()
        ghost.shoot()

    ghost_bonus.changeSpeed(randint(0,3)**3)

    for ghost in Ghosts:
        bullet_touching_ghost = CollisionManager.is_ghost_touched(ghost, bullet_manager)
        if bullet_touching_ghost:
            bullet_manager.delete_player_bullet(bullet_touching_ghost)
            score.add_score_normal()

    player.draw()
    score.show_score()

    bullet_manager.move_and_draw_ghost_bullet()                         # Création des nouveaux tirs
    bullet_manager.move_and_draw_player_bullet()

    if CollisionManager.is_player_touched(player, bullet_manager):      # Collision des tirs
        running = False

    for bullet in bullet_manager.ghost_bullets:
        if bullet.position.y >= screen_height:
            bullet_manager.delete_ghost_bullet(bullet)

    pygame.display.flip()               # Rafraîchissement de l'image
    dt = clock.tick(60) / 1000          # Vitesse de rafraîchissement

pygame.quit()