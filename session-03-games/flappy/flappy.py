import pygame
from pygame.locals import *
import sys

def run():
    screen = pygame.display.set_mode((400, 700))
    clock = pygame.time.Clock()
    background = pygame.image.load("images/background.png").convert()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))

        pygame.display.update()


if __name__ == "__main__":
    run()
