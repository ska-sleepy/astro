import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:

        for event in pygame.event.get(): #check if game is closed
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        
        pygame.Surface.fill(screen, (00,00,00))
        player.draw(screen)
        pygame.display.flip()
        framerate = clock.tick(60)
        dt = framerate / 1000
if __name__ == "__main__":
    main()