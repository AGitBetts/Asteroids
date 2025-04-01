from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        pass

    def draw(self,screen):
        pygame.draw.circle(scree,RGB(255,255,255),(self.x,self.y),self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt
