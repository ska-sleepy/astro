import pygame
import sys
from constants import *
from player import *
from asteroids import *
from asteroField import *
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Shot.containers = (bullets, updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)
    AsteroidField.containers = (updatables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteros = AsteroidField()
    while True:

        for event in pygame.event.get(): #check if game is closed
            if event.type == pygame.QUIT:
                return
        updatables.update(dt)
        for aster in asteroids:
            if aster.check_collisions(player):
                print("Game over!")
                sys.exit()
        for aster in asteroids:
            for bullet in bullets:
                if aster.check_collisions(bullet):
                    aster.kill()
                    bullet.kill()



        
        pygame.Surface.fill(screen, (00,00,00))
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        framerate = clock.tick(60)
        dt = framerate / 1000
if __name__ == "__main__":
    main()