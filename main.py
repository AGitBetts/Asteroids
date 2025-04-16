import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable,drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers  = (updateable)
    Shot.containers = (shots, updateable, drawable)
    player = Player(x,y,shots = shots)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        


        pygame.Surface.fill(screen,(0,0,0,1))

        updateable.update(dt)

        for shot in list(shots):
            if not Shot.within_bounds(shot):
                shot.kill()

        print(f"Number of Asteroids: {len(asteroids)}")
        for asteroid in asteroids:
            check = asteroid.collision(player)
            if check == True:
                sys.exit("Game over!")
            print(f"Number of shots: {len(shots)}")
            for shot in shots:
                if asteroid.collision(shot):
                    print("Hit detected!")
                    asteroid.split(asteroid)
                    shot.kill()

        for item in drawable:
            item.draw(screen)        
        pygame.display.flip()
        clock.tick(60)
        dt = pygame.time.Clock.get_time(clock) / 1000


if __name__ == "__main__":
    main()


