import pygame
import time

pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True

center = (0, 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # Draw this slowly
    pygame.draw.circle(
        screen, (0, 0, 255), center, 75
    )

    if center == (500, 500):
        center = (0, 0)

    center = (center[0] + 1, center[1] + 1)

    time.sleep(0.01)

    pygame.display.flip()

pygame.quit()
