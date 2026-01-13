import pygame
import random
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position = self.position + self.velocity * dt
    
    def split(self):
        self.kill()
        if (ASTEROID_MIN_RADIUS >= self.radius):
            return
        log_event("asteroid_split")
        a1_move = self.velocity.rotate(random.uniform(20, 50))
        a2_move = self.velocity.rotate(random.uniform(20, 50)*-1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = a1_move * 1.2
        a2.velocity = a2_move * 1.2