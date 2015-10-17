#Tron made using Pygame
import pygame
import random
from Player import Player

screen_x = 500
screen_y = 500
size = (screen_x, screen_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tron")
lbound, rbound, ubound, dbound = 0, 490, 0, 490

done = False
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,78,222)
BLUE2 = (111,151,237)
RED = (194,4,36)
RED2 = (237,111,164)
clock = pygame.time.Clock()

#list of things the player can collide with
block_list = pygame.sprite.Group()
#list of everything, including the player
all_sprites_list = pygame.sprite.Group()

#Create both player squares with their trails

player1 = Player(BLUE,10,10)
all_sprites_list.add(player1)
player1.rect.x, player1.rect.y = lbound,ubound
p1Trail = Player(BLUE2,10,10)
p1Trail.rect.x, p1Trail.rect.y = player1.rect.x, player1.rect.y
block_list.add(p1Trail)
all_sprites_list.add(p1Trail)

player2 = Player(RED,10,10)
all_sprites_list.add(player2)
player2.rect.x, player2.rect.y = rbound,dbound
p2Trail = Player(RED2,10,10)
block_list.add(p2Trail)
all_sprites_list.add(p2Trail)

def drawGame():

	#Draw game board grid
	for y_offset in range(0,500,10):
		pygame.draw.line(screen, BLACK, [0,0+y_offset], [500,0+y_offset])
		pygame.draw.line(screen, BLACK, [0+y_offset,0], [0+y_offset, 500])

	
def createTrail(px, py):
		p1Trail = Player(BLUE2,10,10)
		p1Trail.rect.x, p1Trail.rect.y = px, py
		print("PTX:",p1Trail.rect.x,"PTY:",p1Trail.rect.y)
		all_sprites_list.add(p1Trail)
		block_list.add(p1Trail)


def checkBounds():
	if player1.rect.x > rbound:
		player1.rect.x = rbound

	if player1.rect.x < lbound:
		player1.rect.x = lbound

	if player1.rect.y < ubound:
		player1.rect.y = ubound

	if player1.rect.y > dbound:
		player1.rect.y = dbound

	return False


def mainLoop():
	global done, p1_x, p1_y, p2_x, p2_y
	inputMap = [False,False,False,False]

	while not done:
		randMove = random.randint(1,4)

		#Event Processing Loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					#check if player is out of bounds
					checkBounds()
					#move player left
					player1.rect.x -= 10
					#create a trail behind where the player was
					createTrail(player1.rect.x+10, player1.rect.y)
					inputMap = [True,False,False,False]
					#check if there are collisions
					blocks_hit_list = pygame.sprite.spritecollide(player1, block_list, False)
					for block in blocks_hit_list:
						#if there is a collision after going LEFT
						if block.rect.x == player1.rect.x:
							#move the player back right
							player1.rect.x += 10

				if event.key == pygame.K_RIGHT:
					checkBounds()
					player1.rect.x += 10
					createTrail(player1.rect.x-10, player1.rect.y)
					inputMap = [False,True,False,False]
					blocks_hit_list = pygame.sprite.spritecollide(player1, block_list, False)
					for block in blocks_hit_list:
						if block.rect.x == player1.rect.x:
							player1.rect.x -= 10

				if event.key == pygame.K_UP:
					checkBounds()
					player1.rect.y -= 10
					createTrail(player1.rect.x, player1.rect.y+10)
					inputMap = [False,False,True,False]
					blocks_hit_list = pygame.sprite.spritecollide(player1, block_list, False)
					for block in blocks_hit_list:
						if block.rect.y == player1.rect.y:
							player1.rect.y += 10

				if event.key == pygame.K_DOWN:
					checkBounds()
					player1.rect.y += 10
					createTrail(player1.rect.x, player1.rect.y-10)
					inputMap = [False,False,False,True]
					blocks_hit_list = pygame.sprite.spritecollide(player1, block_list, False)
					for block in blocks_hit_list:
						if block.rect.y == player1.rect.y:
							player1.rect.y -= 10

		#playerMove()
		'''if checkBounds() == True:
			if randMove == 1:
				player1.rect.x += 10
				createTrail(player1.rect.x-10, player1.rect.y)
				checkBounds()
				blocks_hit_list = pygame.sprite.spritecollide(player1, block_list, False)
				for block in blocks_hit_list:
					if block.rect.x == player1.rect.x:
						player1.rect.x -= 10
			elif randMove == 2:
				player1.rect.y += 10
				createTrail(player1.rect.x, player1.rect.y-10)
				checkBounds()
				blocks_hit_list = pygame.sprite.spritecollide(player1, block_list, False)
				for block in blocks_hit_list:
					if block.rect.y == player1.rect.y:
						player1.rect.y -= 10
			elif randMove == 3:
				player1.rect.x -= 10
				createTrail(player1.rect.x+10, player1.rect.y)
				checkBounds()
				blocks_hit_list = pygame.sprite.spritecollide(player1, block_list, False)
				for block in blocks_hit_list:
					if block.rect.x == player1.rect.x:
						player1.rect.x += 10
			else:
				player1.rect.y -= 10
				createTrail(player1.rect.x, player1.rect.y+10)
				checkBounds()
				blocks_hit_list = pygame.sprite.spritecollide(player1, block_list, False)
				for block in blocks_hit_list:
					if block.rect.y == player1.rect.y:
						player1.rect.y += 10'''
		
		#For human input, keep moving after button is pressed
		if inputMap[0]:
			checkBounds()
			player1.rect.x -= 10
			createTrail(player1.rect.x+10, player1.rect.y)
			blocks_hit_list = pygame.sprite.spritecollide(player1, block_list, False)
			for block in blocks_hit_list:
				if block.rect.x == player1.rect.x:
					player1.rect.x += 10
		elif inputMap[1]:
			checkBounds()
			player1.rect.x += 10
			createTrail(player1.rect.x-10, player1.rect.y)
			blocks_hit_list = pygame.sprite.spritecollide(player1, block_list, False)
			for block in blocks_hit_list:
				if block.rect.x == player1.rect.x:
					player1.rect.x -= 10
		elif inputMap[2]:
			checkBounds()
			player1.rect.y -= 10
			createTrail(player1.rect.x, player1.rect.y+10)
			blocks_hit_list = pygame.sprite.spritecollide(player1, block_list, False)
			for block in blocks_hit_list:
				if block.rect.y == player1.rect.y:
					player1.rect.y += 10
		elif inputMap[3]:
			checkBounds()
			player1.rect.y += 10
			createTrail(player1.rect.x, player1.rect.y-10)
			blocks_hit_list = pygame.sprite.spritecollide(player1, block_list, False)
			for block in blocks_hit_list:
				if block.rect.y == player1.rect.y:
					player1.rect.y -= 10

		#Clear screen to white
		screen.fill(WHITE)
		drawGame()
		all_sprites_list.draw(screen)

		#Update screen with what we've drawn
		pygame.display.flip()

		#FPS
		clock.tick(15)

	pygame.quit()

mainLoop()