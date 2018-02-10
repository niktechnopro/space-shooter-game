import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,screen,the_player, bullet):
		super(Bullet, self).__init__()
		self.image = pygame.image.load(bullet)
		self.image = pygame.transform.scale(self.image, (20,50))
		self.screen = screen
		self.speed = 15
		self.x = the_player.x + 25
		self.y = the_player.y
		#self.rect = self.image.get_rect()
		self.rect = pygame.Rect(self.x, self.y, 20, 50)

	def update(self):
		self.y -= self.speed
		self.rect = pygame.Rect(self.x, self.y, 20, 50)

	def draw_bullet(self):
		self.screen.blit(self.image,[self.x,self.y])

	def beyond_screen(self):
		if self.y <= 0:
			return True
		return False