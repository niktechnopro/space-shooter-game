# import library of functions
import os
import time
import pygame
import random
from pygame.sprite import Group, groupcollide
from player_ship import Player
from enemies import Enemies
from bullets import Bullet
#initializing game engine
pygame.init()

def beginning():
	os.system("say 'three'")
	os.system("say 'two'")
	os.system("say 'one'")
	os.system("say go")



text_color = (255, 255, 255) #define color with RGB
BLACK = (0,0,0)
size = (800, 800) # width and height tuple as python can not store 2 numbers into 1 variable
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Shooter")#name of the window
done = False #loops until user press the close button
clock = pygame.time.Clock()#manages how fast screen updates
font = pygame.font.SysFont('Calibri', 25, True, False) #select font, and size of text
background = pygame.image.load("images/starBackground.png").convert() #convert is a method of image class
background = pygame.transform.scale(background, (800,800)) #transforms small image to fit game window
beginning()
the_player = Player("images/playerShip.png",350,700,screen)
player_group = Group()
player_group.add(the_player)



#loading all the ships
enemyShip1 = "images/enemyShip.png"
enemyShip2 = "images/enemyShip2.png"
enemyShip3 = "images/enemyShip3.png"
enemyShip4 = "images/enemyShip4.png"

def enemy_ship_selector():
	en_index = random.randint(0,3)
	enemy_images_list = [enemyShip1, enemyShip2, enemyShip3, enemyShip4]
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

def music_effect(effect):
	wins = 0
	if effect == "blaster":
		blaster.play()
	elif effect == "explosion":
		explosion.play()
 
winnings = 0		

#Main Loop
while not done:
	#main event loop
	for event in pygame.event.get(): #user did something
		if event.type == pygame.QUIT: #if user clicked close
			done = True # to exit this loop
		elif event.type == pygame.MOUSEBUTTONDOWN:
			music_effect("blaster")
			new_bullet = Bullet(screen, the_player)
			bullets.add(new_bullet)
	
	#controling a spaceship via the mouse
	player_pos = pygame.mouse.get_pos()
	pygame.mouse.set_visible(False) #to hide the mouse curser
	the_player.update_me(player_pos)

	
	screen.blit(background, [0,0])

	#screen.blit(player_ship, [x, y])
	the_player.draw_me()
	#screen.blit(enemy_ship, [100, 50])
	for enemy_ship in enemy_list:
#		# update the bad guy (based on where the player is)
		enemy_ship.update_me(the_player)
		# draw the bad guy
		enemy_ship.draw_me()
	#bullet portion
	for bullet in bullets:
		# update teh bullet location
		bullet.update()
		# draw the bullet on the screen
		bullet.draw_bullet()

	bullet_hit = groupcollide(bullets, enemy_list, True, True) # when bullet hits the enemy
	for bullet in bullet_hit:
		print "explosion"
		music_effect("explosion")
		winnings += 1
		


	if len(enemy_list) < 4:
		enemy_list.add(Enemies(screen, enemy_ship_selector()))
		enemy_list.add(Enemies(screen, enemy_ship_selector()))

	ship_crash = groupcollide(player_group, enemy_list, True, True) #when enemy ship hits the player
	print ship_crash


	text = font.render("Hits: " + str(winnings), True, text_color)
	screen.blit(text, [600, 50])
	pygame.display.flip() #update the screen  with what we draw
	clock.tick(30) #number of frames per second


pygame.quit()