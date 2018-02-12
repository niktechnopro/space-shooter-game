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

bckg_y = 0 # initial position of the background
text_color = (255, 255, 255) #define color with RGB
BLACK = (0,0,0)
YELLOW = (255,255,0)
width = 800 # x size of the screen
height = 800 # y size of the screen
size = (width, height) # width and height tuple as python can not store 2 numbers into 1 variable
font = pygame.font.SysFont('Calibri', 25, True, False) #select font, and size of text
font1 = pygame.font.Font('font/font.ttf', 40) #font
font2 = pygame.font.Font('font/font.ttf', 20) #font
font3 = pygame.font.Font('font/font.ttf', 15) #font
screen = pygame.display.set_mode(size) #screen is going to be a Surface class
pygame.display.set_caption("Space Shooter")#name of the window
clock = pygame.time.Clock()#manages how fast screen updates
background = pygame.image.load("images/starBackground.png").convert() #convert is a method of image class
background = pygame.transform.scale(background, (width,height)) #transforms small image to fit game window
background2 = background #creating second background image
the_player = Player("images/playerShip.png",350,700,screen)
player_group = Group()
player_group.add(the_player)

#function to exit
def quit():
	pygame.quit()
	sys.exit()

#save record
def saveRecord(score):
	file = open('scores.txt', 'w')
	file.write(str(score))
	file.close()

#load record
def loadRecord():
	file = open('scores.txt', 'r')
	data = file.read()
	file.close()
	return data

record = int(loadRecord())
#loading all the ships
enemyShip1 = "images/enemyShip.png"
enemyShip2 = "images/enemyShip2.png"
enemyShip3 = "images/enemyShip3.png"
enemyShip4 = "images/enemyShip4.png"
enemyShip5 = "images/enemyShip5.png"
enemyShip6 = "images/enemyShip6.png"

def enemy_ship_selector():
	en_index = random.randint(0,5)
	enemy_images_list = [enemyShip1, enemyShip2, enemyShip3, enemyShip4, enemyShip5, enemyShip6]
	enemy_ship_selector = enemy_images_list[en_index]
	return enemy_ship_selector
enemy_ship = Enemies(screen, enemy_ship_selector())
 #call function to select enemy ships combination
enemy_list = Group() #creates list of sprites which is managed by class 'Group'
for i in range(random.randint(3, 9)):
	 # this represents an enemy
	enemy_list.add(enemy_ship)

#initial bullet
bullet_image = "images/spacebullet1.png"

def bullet_selector(score):
	if score < 8:
		bullet_image = "images/spacebullet1.png"
	elif score >=8 and score < 16:
		bullet_image = "images/spacebullet2.png"
	elif score >= 16 and score < 24:
		bullet_image = "images/spacebullet3.png"
	else:
		bullet_image = "images/spacebullet4.png"
	return bullet_image

new_bullet = Bullet(screen, the_player, bullet_image)
bullets = Group()


blaster = pygame.mixer.Sound('sounds/blaster.wav')#using Sound class does not interrupt main music
explosion = pygame.mixer.Sound('sounds/explosion.wav')

# def beginning():
# 	os.system("say 'three'")
# 	os.system("say 'two'")
# 	os.system("say 'one'")
# 	os.system("say 'go'")

#the following function would draw the text
def print_text(msg, pos, _font, color = (0,0,0), bgcolor = (255,255,255)):
	text = _font.render(msg, True, color)
	screen.blit(text, pos)

#first page
def showIntro():
	print_text("WELCOME TO SPACESHOOTER", (40, 100), font1, text_color)
	print_text("PRESS SPACE TO START!", (115, 550), font1, text_color)
	print_text("Shoot as many enemy ships as you can", (140, 200), font2, YELLOW)
	print_text("Press 'P' to pause at any time", (200, 250), font2, text_color)
	print_text("Game Over if:", (140, 350), font2, YELLOW)
	print_text("* One enemy ship passes you", (140, 400), font2, YELLOW)
	print_text("* Enemy ships collides with you", (140, 450), font2, YELLOW)
	print_text("Press ESC to exit at any time", (450, 750), font, text_color)

def music_effect(effect):  #function to pull up sound effects
	wins = 0
	if effect == "blaster":
		blaster.play()
	elif effect == "explosion":
		explosion.play() 

#drawing and moving the background
def moving_background(bckg_y):
	rel_y = bckg_y % background.get_rect().height
	screen.blit(background, [0, rel_y - background.get_rect().height])
	if rel_y > 0:
		screen.blit(background2,(0, rel_y))
	bckg_y += 1

def game_over(score):
	bckg_y = 0
	if score > record:
		saveRecord(score)	
	while True:
		moving_background(bckg_y)
		bckg_y += 1
		for event in pygame.event.get():
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_ESCAPE:
					quit()
			elif event.type == pygame.QUIT:
				quit()
		print_text("Game Over!", (280, 400), font1, text_color)
		print_text("Highest Score Achieved: " + str(record), (241, 500), font2, YELLOW)
		print_text("Your Score: " + str(score), (332, 600), font2, text_color)
		print_text("Press ESC to exit", (50, 50), font, text_color)
		pygame.display.flip()
	# main_game(False)

def pause():
	print "pause activated"
	pause = True
	while pause:
		print_text("Game Paused", (240, 400), font1, text_color)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					return
				if event.key == pygame.K_ESCAPE:
					quit()
			elif event.type == pygame.QUIT:
				quit()
		pygame.display.update()
		clock.tick(15)


	
#First page loop
intro = True
while intro:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				print "space pressed"
				intro = False
			if event.key == pygame.K_ESCAPE:
				quit()
		elif event.type == pygame.QUIT:
			quit()
	moving_background(bckg_y)
	bckg_y += 1
	showIntro()
	pygame.display.update()
	clock.tick(15)

# loading game music
pygame.mixer.music.load("sounds/music.wav") #load game music
pygame.mixer.music.play(-1) #'-1' means play indefinetely
#Main Loop
def main_game(val):
#	variables used in this function
	winings = 0
	ships_missed = 0
	bckg_y = 0	
	while val:
		#main event loop
		

		for event in pygame.event.get(): #user did something
			if event.type == pygame.QUIT: #if user clicked close
				done = True # to exit this loop
			elif event.type == pygame.KEYDOWN:
				if event.key == K_ESCAPE:
					# sys.exit()
					quit()
				if event.key == pygame.K_p:
					print "hitting button P"#just a test for now
					pause()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				music_effect("blaster")
				new_bullet = Bullet(screen, the_player, bullet_selector(winings))
				bullets.add(new_bullet)
		
		#controling a spaceship via the mouse
		player_pos = pygame.mouse.get_pos()
		pygame.mouse.set_visible(False) #to hide the mouse curser
		the_player.update_me(player_pos)

		#drawing and moving the background
		moving_background(bckg_y)
		bckg_y += 1
		#screen.blit(player_ship, [x, y])
		the_player.draw_me()
		#screen.blit(enemy_ship, [100, 50])
		for enemy_ship in enemy_list:
			# update the bad guy (based on where the player is)
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
			#remove bullet if beyond the screen
			if bullet.beyond_screen():
				bullets.remove(bullet)
				print "bullet removed"


		#enemy collision with bullet
		bullet_hit = groupcollide(bullets, enemy_list, True, True) # when bullet hits the enemy
		for bullet, enemy_ship in bullet_hit.iteritems():
			print "explosion"
			music_effect("explosion")
			enemy_ship[0].explosions()
			winings += 1
			

		if len(enemy_list) < 4:											#if number of ships on the screen gets less than 4 - generate another ship
			enemy_list.add((Enemies(screen, enemy_ship_selector())))
			enemy_list.add((Enemies(screen, enemy_ship_selector())))
		
		player_crash = groupcollide(player_group, enemy_list, True, True) #when enemy ship hits the player
		for player, enemy_ship in player_crash.iteritems():
			print "player hit"
			music_effect("explosion")
			player.explosions()
			game_over(winings)


		print_text("Hits: " + str(winings), (600, 50), font, text_color)

		print_text("Ships missed: " + str(ships_missed), (100, 50), font, text_color)

		print_text("Press ESC to exit at any time", (450, 750), font, text_color)
		
		if ships_missed >= 1:
			game_over(winings)
		
		pygame.display.update() #update the screen  with what we draw
		clock.tick(40) #number of frames per second

main_game(True)#keeping the main game loop running


