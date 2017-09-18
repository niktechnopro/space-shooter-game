import pygame
from pygame.sprite import Sprite
from math import hypot
import random

class Enemy_list(Sprite):
	def __init__(self,screen):
		super(Enemies,self).__init__()
		self.image = pygame.image.load("images/enemyShip.png")
		self.x = random.randrange(0,730,100)
		self.y = 10
		self.screen = screen
		self.speed = 2
		self.rect = self.image.get_rect()
enemy_list = pygame.sprite.Group() #creates list of sprites which is managed by class 'Group'
for i in range(random.randint(1, 9)):
	enemy_ship = Enemies(screen) # this represents an enemy
	enemy_list.add(enemy_ship)





	!/usr/bin/env python

import random #as explained above
from helpers import *

class Space1(pygame.sprite.Sprite):
    def __init__(self, i):                      
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("space.png", 10)
        self.dx = -5
        self.reset(i)

    def update(self, i):
        self.rect.top += self.dx
        if i == 1:
            if self.rect.top <= -600:
                self.__init__(i) 
        else:
            if self.rect.top <= -1200:
                self.__init__(i) 

    def reset(self, i):
        if i == 1:
            self.rect.top = 1
        else:
            self.rect.top = 300

class Space2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("space.png", 10)
        self.dx = -5
        self.reset()

    def update(self):
        self.rect.top += self.dx
        if self.rect.top <= -1200:
            self.__init__() 

    def reset(self):
        self.rect.top = 600

class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_image('ship.gif', -1)
        self.x_dist = 5
        self.y_dist = 5
        self.lasertimer = 0
        self.lasermax = 5
        self.rect.centery = 400
        self.rect.centerx = 400

    def update(self):
        key = pygame.key.get_pressed()

        # Movement
        if key[K_UP]:
            self.rect.centery += -3
        if key[K_DOWN]:
            self.rect.centery += 3
        if key[K_RIGHT]:
            self.rect.centerx += 3
        if key[K_LEFT]:
            self.rect.centerx += -3

        # Lasers
        if key[K_SPACE]:
            self.lasertimer = self.lasertimer + 1
            if self.lasertimer == self.lasermax:
                laserSprites.add(Laser(self.rect.midtop))
                self.lasertimer = 0

        # Restrictions
        self.rect.bottom = min(self.rect.bottom, 600)
        self.rect.top = max(self.rect.top, 0)
        self.rect.right = min(self.rect.right, 800)
        self.rect.left = max(self.rect.left, 0)

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("laser.png", -1)
        self.rect.center = pos

    def update(self):
        if self.rect.right > 800:
            self.kill()
        else:
            self.rect.move_ip(0, -15)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("alien.png", -1)
        self.rect = self.image.get_rect()
        self.dy = 8
        self.reset()

    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top > 600:
            self.reset()

        # Laser Collisions    
        if pygame.sprite.groupcollide(enemySprites, laserSprites, 1, 1):
           explosionSprites.add(EnemyExplosion(self.rect.center))
           ###################################################
           ###---LOOK HERE - I've added two lines here  ---###
           ###---First you need to replace this sprite  ---###
           ###---before removing it, then you need to   ---###
           ###---remove this sprite from the group      ---###
           ###################################################