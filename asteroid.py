import pygame
from circleshape import CircleShape
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
        old_position = self.position
        self.kill()
        #print(f"Old Position: {old_position}")
        if  ASTEROID_MIN_RADIUS > self.radius:
            return
        angle = random.uniform(20,50)
        splitvect_1  = self.velocity.rotate(angle)
        splitvect_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_ast1 = Asteroid(old_position.x, old_position.y, new_radius)
        split_ast1.velocity = splitvect_1 * 1.2
        split_ast2 = Asteroid(old_position.x, old_position.y, new_radius)
        split_ast2.velocity = splitvect_2 * 1.2
        
        

