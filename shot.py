from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
 


    def draw(self, screen):
        center = (self.position.x,self.position.y)
        color = (255, 255, 255)
        pygame.draw.circle(screen, color, center, self.radius, width=2)

    def update(self, dt):    
        self.position +=(self.velocity * dt)
    
