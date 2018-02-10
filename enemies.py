import pygame
from pygame.sprite import Sprite
from math import hypot
import random

#creating explosion list
explosion_list = []
image_exposion_one = pygame.image.load("./images/explosion/exp1.png")
explosion_list.append(image_exposion_one);
image_exposion_two = pygame.image.load("./images/explosion/exp2.png")
explosion_list.append(image_exposion_two);
image_exposion_three = pygame.image.load("./images/explosion/exp3.png")
explosion_list.append(image_exposion_three);
image_exposion_four = pygame.image.load("./images/explosion/exp4.png")
explosion_list.append(image_exposion_four);
image_exposion_five = pygame.image.load("./images/explosion/exp5.png")
explosion_list.append(image_exposion_five);
image_exposion_six = pygame.image.load("./images/explosion/exp6.png")
explosion_list.append(image_exposion_six);
image_exposion_seven = pygame.image.load("./images/explosion/exp7.png")
explosion_list.append(image_exposion_seven);
image_exposion_eight = pygame.image.load("./images/explosion/exp8.png")
explosion_list.append(image_exposion_eight);
image_exposion_nine = pygame.image.load("./images/explosion/exp9.png")
explosion_list.append(image_exposion_nine);

class Enemies(Sprite):
	def __init__(self, screen, image):
		super(Enemies,self).__init__()
		self.image = pygame.image.load(str(image))
		self.image = pygame.transform.scale(self.image, (70, 70))
		self.x = random.randrange(10,730,100)
		self.y = 10
		self.screen = screen
		self.speed = random.randrange(2,3,1)
		#self.rect = self.image.get_rect()
		self.rect = pygame.Rect(self.x, self.y, 90, 70)
		self.ships_missed = 0
		

	def update_me(self, the_player):
		self.y += self.speed
		#self.rect.top = self.y
		self.rect = pygame.Rect(self.x, self.y, 90, 70)
		

	def draw_me(self):
		self.screen.blit(self.image,[self.x,self.y])

	def explosions(self, bullet): #later on will go for coordinates( w, h ):
		counter = 0
		for i in range(0, 800):
			if i%100 == 0:
				counter += 1
			self.screen.blit(explosion_list[counter], (self.x , self.y) )

	def beyond_screen(self):
		if self.y >= 780:
			return True
		return False



	

