import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

screen = pygame.display.set_mode([500, 500])
screen.fill((255, 255, 255))

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            runninge = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_UP:
                print("Up key pressed")
            elif event.key == K_DOWN:
                print("Down key pressed")
            elif event.key == K_LEFT:
                print("Left key pressed")
            elif event.key == K_RIGHT:
                print("Right key pressed")

    pygame.display.flip()

pygame.quit()
