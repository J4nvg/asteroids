import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots,updatable,drawable)
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    AsteroidField.containers = (updatable )
    Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for item in updatable:
            item.update(dt)
        for item in drawable:
            item.draw(screen)
        for a in asteroids:
            for shot in shots:
                if a.check_collision(shot):
                    a.split()
                    shot.kill()
            if a.check_collision(player):
                print("Game over!") 
                exit()
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # print(f"Starting asteroids!")

if __name__ == "__main__":
    main()