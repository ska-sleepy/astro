import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:

        for event in pygame.event.get(): #check if game is closed
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (00,00,00))
        pygame.display.flip()


if __name__ == "__main__":
    main()