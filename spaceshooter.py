# import library of functions
import os
import sys
import time
import pygame
import random
from pygame.sprite import Group, groupcollide
from player_ship import Player
from enemies import Enemies
from bullets import Bullet
from pygame.constants import K_ESCAPE
#initializing game engine
pygame.init()

def beginning():
	os.system("say 'three'")
	os.system("say 'two'")
	os.system("say 'one'")
	os.system("say go")


text_color = (255, 255, 255) #define color with RGB
BLACK = (0,0,0)
width = 800 # x size of the screen
height = 800 # y size of the screen
size = (width, height) # width and height tuple as python can not store 2 numbers into 1 variable
screen = pygame.display.set_mode(size) #screen is going to be a Surface class
pygame.display.set_caption("Space Shooter")#name of the window
done = False #loops until user press the close button
clock = pygame.time.Clock()#manages how fast screen updates
font = pygame.font.SysFont('Calibri', 25, True, False) #select font, and size of text
background = pygame.image.load("images/starBackground.png").convert() #convert is a method of image class
background = pygame.transform.scale(background, (width,height)) #transforms small image to fit game window
background2 = background #creating second background image
#beginning()
the_player = Player("images/playerShip.png",350,700,screen)
player_group = Group()
player_group.add(the_player)



#loading all the ships
enemyShip1 = "images/enemyShip.png"
enemyShip2 = "images/enemyShip2.png"
enemyShip3 = "images/enemyShip3.png"
enemyShip4 = "images/enemyShip4.png"
enemyShip5 = "images/enemyShip5.png"

def enemy_ship_selector():
	en_index = random.randint(0,4)
	enemy_images_list = [enemyShip1, enemyShip2, enemyShip3, enemyShip4, enemyShip5]
	enemy_ship_selector = enemy_images_list[en_index]
	return enemy_ship_selector

enemy_ship = Enemies(screen, enemy_ship_selector())
 #call function to select enemy ships combination
enemy_list = Group() #creates list of sprites which is managed by class 'Group'
for i in range(random.randint(3, 9)):
	 # this represents an enemy
	enemy_list.add(enemy_ship)

new_bullet = Bullet(screen, the_player)
bullets = Group()


pygame.mixer.music.load("sounds/music.wav") #load game music
pygame.mixer.music.play(-1) #'-1' means play indefinetely

blaster = pygame.mixer.Sound('sounds/blaster.wav')#using Sound class does not interrupt main music
explosion = pygame.mixer.Sound('sounds/explosion.wav')

def music_effect(effect):  #function to pull up sound effects
	wins = 0
	if effect == "blaster":
		blaster.play()
	elif effect == "explosion":
		explosion.play()
now = time.time() 
winnings = 0
ships_missed = 0		
bckg_y = 0
#Main Loop
while not done:
	#main event loop
	

	for event in pygame.event.get(): #user did something
		if event.type == pygame.QUIT: #if user clicked close
			done = True # to exit this loop
		elif event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			music_effect("blaster")
			new_bullet = Bullet(screen, the_player)
			bullets.add(new_bullet)
	
	#controling a spaceship via the mouse
	player_pos = pygame.mouse.get_pos()
	pygame.mouse.set_visible(False) #to hide the mouse curser
	the_player.update_me(player_pos)
	
#	screen.blit(background, [0,0])
	#drawing and moving the background
	rel_y = bckg_y % background.get_rect().height
	#print rel_y
	screen.blit(background, [0, rel_y - background.get_rect().height])
	if rel_y > 0:
		screen.blit(background2,(0, rel_y))
	bckg_y += 1

	#screen.blit(player_ship, [x, y])
	the_player.draw_me()
	#screen.blit(enemy_ship, [100, 50])
	for enemy_ship in enemy_list:
#		# update the bad guy (based on where the player is)
		enemy_ship.update_me(the_player)
		# draw the bad guy
		enemy_ship.draw_me()
		if enemy_ship.beyond_screen():
			ships_missed += 1
			enemy_list.remove(enemy_ship)
			print "ship missed"
			

	#bullet portion
	for bullet in bullets:
		# update teh bullet location
		bullet.update()
		# draw the bullet on the screen
		bullet.draw_bullet()



	bullet_hit = groupcollide(bullets, enemy_list, True, True) # when bullet hits the enemy
	for bullet, enemy_ship in bullet_hit.iteritems():
		print "explosion"
		music_effect("explosion")
		enemy_ship[0].explosions(bullet)
		winnings += 1
		

	if len(enemy_list) < 4:											#if number of ships on the screen gets less than 4 - generate another ship
		enemy_list.add((Enemies(screen, enemy_ship_selector())))
		enemy_list.add((Enemies(screen, enemy_ship_selector())))
	

	

	ship_crash = groupcollide(player_group, enemy_list, True, True) #when enemy ship hits the player
	print ship_crash

	text = font.render("Hits: " + str(winnings), True, text_color)# these 2 lines display a text for wins in the right top side of screen
	screen.blit(text, [600, 50])

	text = font.render("Ships missed: " + str(ships_missed), True, text_color)# these 2 lines display a text for wins in the right top side of screen
	screen.blit(text, [100, 50])
	
	if ships_missed >= 5:
		end_game()

	pygame.display.update() #update the screen  with what we draw
	clock.tick(80) #number of frames per second
	def end_game():
		while time.time() < now + 5:
			text = font.render("Game Over", True, text_color)# these 2 lines display a text for wins in the right top side of screen
			return text
			screen.blit(text, [400, 400])
			pygame.display.update() #update the screen  with what we draw
		quit()

pygame.quit()