import pygame
import random

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,78,222)
RED = (194,4,36)

class Player(pygame.sprite.Sprite):

	def __init__(self, color, width, height):

		#Call parent class (Sprite) constructor
		super().__init__()

		#Set background color, and set to transparent
		self.image = pygame.Surface([width, height])
		self.image.fill(WHITE)
		self.image.set_colorkey(WHITE)

		#Draw the square
		pygame.draw.rect(self.image, color, [0,0,width,height])

		#Needed to move the sprite
		self.rect = self.image.get_rect()

