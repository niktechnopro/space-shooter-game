import pygame
from pygame.sprite import Sprite
BLACK = (0,0,0)
class Player(Sprite):
	# Classes always contain 2 parts:
	# 1. the __init__ section where you define all attributes. 
	# Init, only runs once. When the object is instantiated
	# Because this is a subclass, we need to call the parent's (Sprite) __init__
	def __init__(self,image,start_x,start_y,screen):
		super(Player,self).__init__()
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image,(70,70))
		self.x = start_y
		self.y = start_y
		self.screen = screen
		self.rect = pygame.Rect(self.x, self.y, 70, 70)

	def update_me(self,player_pos):
		self.x = player_pos[0]
		self.y = player_pos[1]
		if self.x > 730:
			self.x = 730
		elif self.y > 700:
			self.y = 700
		else:
			self.x = player_pos[0]
			self.y = player_pos[1]
		self.rect = pygame.Rect(self.x, self.y, 70, 70)

		

	# 2. The methods where you define all the class functions (methods)
	def draw_me(self,):
		self.screen.blit(self.image, [self.x,self.y])
		


	