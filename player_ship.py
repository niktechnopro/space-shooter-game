import pygame
from pygame.sprite import Sprite
BLACK = (0,0,0)

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
		self.winings = 0

	def update_me(self,player_pos):
		self.x = player_pos[0]
		self.y = player_pos[1]
		if self.x > 730:             #set up the boundaries of the ship
			self.x = 720
		elif self.x < 10:
			self.x = 10
		elif self.y > 700:
			self.y = 700
		elif self.y < 10:
			self.y = 10
		else:
			self.x = player_pos[0]
			self.y = player_pos[1]
		self.rect = pygame.Rect(self.x, self.y, 70, 70)

	def explosions(self): #later on will go for coordinates( w, h ):
		counter = 0
		for i in range(0, 8, 1):
			counter += 1
			self.screen.blit(explosion_list[counter], (self.x , self.y) )
		
	# 2. The methods where you define all the class functions (methods)
	def draw_me(self,):
		self.screen.blit(self.image, [self.x,self.y])

	def winings(self):
		self.winings += 1
		


	