import pygame
from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self,x,y,radius):
        CircleShape.__init__(self,x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),(self.position.x,self.position.y),self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def within_bounds(self):
        return 0 <= self.position.x <= SCREEN_WIDTH and 0 <= self.position.y <= SCREEN_HEIGHT
