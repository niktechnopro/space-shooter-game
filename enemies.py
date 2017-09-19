import pygame
from pygame.sprite import Sprite
from math import hypot
import random


class Enemies(Sprite):
	def __init__(self, screen, image):
		super(Enemies,self).__init__()
		self.image = pygame.image.load(str(image))
		self.image = pygame.transform.scale(self.image, (70, 70))
		self.x = random.randrange(0,730,100)
		self.y = 10
		self.screen = screen
		self.speed = 2
		#self.rect = self.image.get_rect()
		self.rect = pygame.Rect(self.x, self.y, 90, 70)
		

	def update_me(self, the_player):
		self.y += self.speed
		#self.rect.top = self.y
		self.rect = pygame.Rect(self.x, self.y, 90, 70)
		

	def draw_me(self):
		self.screen.blit(self.image,[self.x,self.y])

	def explosion(self, bullets_x, bullets_y):
		self.image = pygame.image.load("images/explosion.png")
		bullets_x = self.x
		bullets_y = self.y

	

