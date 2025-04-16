from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        CircleShape.__init__(self,x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),(self.position.x,self.position.y),self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self,dt):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            v1 = self.velocity.rotate(random_angle)
            v2 = self.velocity.rotate(-random_angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, new_rad)
            a2 = Asteroid(self.position.x, self.position.y, new_rad) 
            a1.velocity = v1
            a2.velocity = v2
