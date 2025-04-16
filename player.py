from circleshape import CircleShape
from constants import *
from shot import *
import pygame

class Player(CircleShape):
    def __init__(self,x,y,shots):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.shots = shots
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen, (255,255,255,1),self.triangle(),2)
    
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self,dt):
        if self.timer > 0:
            self.timer -= dt

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE] and self.timer <= 0:    
            self.shoot(dt)
       
    def move(self,dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self,dt):
        new_shot = Shot(self.position.x,self.position.y, SHOT_RADIUS)
        velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        new_shot.velocity = velocity
        self.timer = PLAYER_SHOOT_COOLDOWN
        self.shots.add(new_shot)

   
