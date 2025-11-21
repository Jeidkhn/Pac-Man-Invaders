from random import randint
import pygame                                                       # Imports de fichiers
import BonusManager
import Player
import Ghost
import BulletManager
import Score
import CollisionManager
import Bonus

pygame.init()
screen_height = 720
screen_width = 960
screen = pygame.display.set_mode((screen_width, screen_height))    # Taille d'écran rétro
clock = pygame.time.Clock()     # Le temps du jeu
dt = 0.0                                          # Variables
running = True
timer = 0

bullet_manager = BulletManager.BulletManager(screen)
bonus_manager = BonusManager.BonusManager(screen)

bonus = None
bullet_touching_bonus = None

ghost1 = Ghost.Ghost(
    130,
    100,
    "right",
    "rose",
    (50, 60),
    screen,
    3,
    pygame.Vector2(130, 100),
    pygame.Vector2(130, 290),
    pygame.Vector2(780, 290),
    pygame.Vector2(780, 100),
    bullet_manager,
    0,
    120
)

ghost2 = Ghost.Ghost(
    550,
    100,
    "right",
    "rouge",
    (50, 60),
    screen,
    3,
    pygame.Vector2(130, 100),
    pygame.Vector2(130, 290),
    pygame.Vector2(780, 290),
    pygame.Vector2(780, 100),
    bullet_manager,
    0,
    180
)

ghost3 = Ghost.Ghost(
    780,
    290,
    "left",
    "cyan",
    (50, 60),
    screen,
    3,
    pygame.Vector2(130, 100),
    pygame.Vector2(130, 290),
    pygame.Vector2(780, 290),
    pygame.Vector2(780, 100),
    bullet_manager,
    0,
    150
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
    90
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

Ghosts = [ghost1, ghost2, ghost3, ghost4]

while running == True:                   # Tant que le jeu tourne, la variable est vrai
    for event in pygame.event.get():
        if event.type == pygame.QUIT:    # Si l'écran d'affichage est supprimé, arrêt du jeu, car variable devient fausse
            running = False

    screen.fill("black")

    keys = pygame.key.get_pressed()                                     # Déplacement du joueur
    if keys[pygame.K_w]:
        player.shoot()

    if keys[pygame.K_a]:
        player.move_left()

    if keys[pygame.K_d]:
        player.move_right()

    for ghost in Ghosts:                                                # Fonctionnement du fantôme
        ghost.draw()
        ghost.move()
        ghost.shoot()

    for ghost in Ghosts:
        bullet_touching_ghost = CollisionManager.is_ghost_touched(ghost, bullet_manager)
        if bullet_touching_ghost:
            bullet_manager.delete_player_bullet(bullet_touching_ghost)
            score.add_score_normal()

    if timer >= 10:
        if not bonus:
            print("added bonus")

            bonus = Bonus.Bonus(
                360,
                200,
                "white",
                (30, 30),
                screen,
                7,
                pygame.Vector2(190, 200),
                pygame.Vector2(720, 200),
                0
            )

            bonus_manager.add_new_bonus(bonus)


    if bonus:
        bullet_touching_bonus = CollisionManager.is_bonus_touched(bonus, bullet_manager)
        bonus_manager.move_and_draw_bonus()
        bonus.change_speed(randint(1, 5) ** 2)

    if bullet_touching_bonus:
        print("bullet touched")
        score.add_score_bonus()
        bonus_manager.delete_bonus()
        bonus = None
        timer = 0
        bullet_touching_bonus = False

    player.draw()
    score.show_score()

    bullet_manager.move_and_draw_ghost_bullet()                         # Création des nouveaux tirs
    bullet_manager.move_and_draw_player_bullet()

    if CollisionManager.is_player_touched(player, bullet_manager):      # Collision des tirs
        running = False

    for bullet in bullet_manager.ghost_bullets:                         # Tirs hors-écrans supprimés
        if bullet.position.y >= screen_height:
            bullet_manager.delete_ghost_bullet(bullet)

    for bullet in bullet_manager.player_bullets:
        if bullet.position.y <= 0:
            bullet_manager.delete_player_bullet(bullet)


    pygame.display.flip()               # Rafraîchissement de l'image
    timer += dt
    dt = clock.tick(60) / 1000          # Vitesse de rafraîchissement

pygame.quit()