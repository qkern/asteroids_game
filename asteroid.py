import random
from circleshapes import *
from constants import *

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
            return []
        new_asteroids = []
        base_angle = random.uniform(20, 50)
        angles = [self.velocity.rotate(base_angle), self.velocity.rotate(-base_angle)]
        for angle in angles:
            asteroid = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            asteroid.velocity = angle * ASTEROID_SPLIT_SPEED
            new_asteroids.append(asteroid)
        return new_asteroids
    