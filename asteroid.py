from circleshape import *
import pygame
import random
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.radius = radius
        self.x = x
        self.y = y
    def draw(self, screen):
        center = (self.position.x,self.position.y)
        color = (255, 255, 255)
        pygame.draw.circle(screen, color, center, self.radius, width=2)        
    def update(self, dt):    
        self.position +=(self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rand_trajectory = random.uniform(20, 50)

        a = self.velocity.rotate(rand_trajectory)
        b = self.velocity.rotate(-rand_trajectory)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2