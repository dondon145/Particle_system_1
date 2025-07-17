import pygame
import math

class Particle(pygame.sprite.Sprite):

    def remove_from_list(self, list):
        if self.life < 0 :
            list.remove(self)

    def set_color(self):
        color = self.color
        del color[3]
        color.append(self.alpha*255)
        self.color = color

    def set_alpha(self):
        self.alpha = self.age_ratio
    
    def get_age_ratio(self):
        self.age_ratio = self.life/self.original_life

    def add_time(self, delta_time):
        self.life -= delta_time
        self.time += delta_time

    def update(self):
        # 1/60/60 - every second there plays 60 frames, the other division by 120 is here just to make it go slower as of my desire
        if self.life > 0:
            self.add_time(0.01)
            self.pos_x += self.velocity['x']* self.time
            self.pos_y += self.velocity['y']* self.time
            self.rect.center = (self.pos_x, self.pos_y)
            self.set_color()
            self.get_age_ratio()
            self.set_alpha()
            self.image.fill(self.color)
            self.image.set_alpha(self.alpha*255)
        else:
            self.kill()
            self.remove_from_list(self.list)
            

    def __init__(self, color, surface_width, surface_height, pos_x, pos_y, speed, angle, life, my_list):
        super().__init__()

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.vel_x = speed* math.cos(angle)
        self.vel_y = -1* speed* math.sin(angle)
        self.velocity = {"x": self.vel_x, "y": self.vel_y}
        
        self.time = 0
        self.life = self.original_life = life
        self.alpha = self.age_ratio = 1
        self.color = []
        self.color = color
        #self.set_color()

        self.list = my_list

        self.image = pygame.Surface((surface_width, surface_height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)