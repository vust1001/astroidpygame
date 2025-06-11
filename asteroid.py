from circleshape import *
import pygame

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
        