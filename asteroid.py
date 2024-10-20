from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)
        rnew = self.radius - ASTEROID_MIN_RADIUS
        newAs1 = Asteroid(*self.position,rnew)
        newAs2 = Asteroid(*self.position,rnew)
        newAs1.velocity = v1 * 1.2
        newAs2.velocity = v2 * 1.2
    def draw(self,screen):
        pygame.draw.circle(screen,"white",(self.position),self.radius,2)
    def update(self,dt):
        self.position += self.velocity * dt

