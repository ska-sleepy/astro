import pygame
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:

        for event in pygame.event.get(): #check if game is closed
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (00,00,00))
        pygame.display.flip()
        framerate = clock.tick(60)
        dt = framerate / 1000

if __name__ == "__main__":
    main()