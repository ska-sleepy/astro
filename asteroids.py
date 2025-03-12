from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return "this was a small asteroid were done"
        else:
            random_angle = random.uniform(20, 30)
            vel1 = self.velocity.rotate(random_angle)
            vel2 = self.velocity.rotate(-random_angle)

            self.radius -= ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius)
            asteroid1.velocity = vel1 * 1.2
            asteroid2.velocity = vel2 * 1.2

    
    

