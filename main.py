# use code form open-source pygame library
import pygame

# using constants from constants.py
from constants import *

from logger import log_state

pygame.init()
Clock = pygame.time.Clock()

def main():
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()
        # last line of loop, sets fps
        dt = Clock.tick(60) / 1000

if __name__ == "__main__":
    main()
