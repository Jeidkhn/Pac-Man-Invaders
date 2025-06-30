import pygame

pygame.init()
screen = pygame.display.set_mode((960, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.1)
player_width = 40

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("blue")

    pygame.draw.circle(screen, "yellow", player_pos, player_width)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player_pos.x -= 600 * dt
    if keys[pygame.K_d]:
        player_pos.x += 600 * dt

    player_pos.x = max(player_width, min(960-player_width, player_pos.x))

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()