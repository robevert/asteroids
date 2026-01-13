# use code form open-source pygame library
import pygame
import sys

# using constants from constants.py
from constants import *
from player import *
from shot import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

from logger import log_state
from logger import log_event

pygame.init()
Clock = pygame.time.Clock()

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group() 
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for roid in asteroids:
            if roid.collides_with(player):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        for roid in asteroids:
            for shot in shots:
                if shot.collides_with(roid):
                    log_event("asteroid_shot")
                    shot.kill()
                    roid.split()
        log_state()
        screen.fill((0, 0, 0))
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        # last line of loop, sets fps
        dt = Clock.tick(60) / 1000

if __name__ == "__main__":
    main()
