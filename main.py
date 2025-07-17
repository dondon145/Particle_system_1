import pygame
from pygame.locals import *
import particle
import random

pygame.init()

DISPLAYWIDTH = 800
DISPLAYHEIGHT = 800

DISPLAY = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))

# colors 
BLACK = [0, 0, 0]
RED = [255, 0, 0, 255]
BLUE = [0, 0, 255, 255]
GREEN = [0, 255, 0, 255]

#obj = particle.Particle(RED, 30, 30, 400, 400, 0.2, 45, 5)
moving_group = pygame.sprite.Group()

particles = []


running = True

while running :
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            for i in range(30):
                obj = particle.Particle(RED, 30, 30, 400, 400, random.randrange(1, 2)/5, random.randrange(-180, 180), 5, particles)
                particles.append(obj)
                moving_group.add(particles[i])

    DISPLAY.fill(BLACK)
    moving_group.update()
    moving_group.draw(DISPLAY)

    
    pygame.display.flip()