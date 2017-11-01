
import pygame
from pygame.locals import *
from constantes import *


class Level:
	
	def __init__(self, file):
		self.file = file
		self.structure = 0

	# on ouvre le fichier qui contient le niveau
	# on intialise une variable level_structure qui contient une liste vide
	# on lit chaque ligne du fichier et on créé une liste vide pour chaque ligne
	# pour chaque sprite de la ligne qui est différent de "\n" on ajoute la valeur du sprite dans la liste de la ligne
	# on ajoute chaque ligne à la liste level_structure
	# self.structure à maintenant pour valeur level_structure (donc une liste qui contient plusieurs lignes de listes qui elles-mêmes contiennent la valeur de chaque sprite de cette ligne)
	def level_generation(self):
		# open a file
		with open(self.file, "r") as file:
			level_structure = []
			for line in file:
				level_line = []
				for sprite in line:
					if sprite != '\n':
						level_line.append(sprite)
				level_structure.append(level_line)
			self.structure = level_structure


	def show_level(self, window):
		wall = pygame.image.load(wall_image).convert()
		start = pygame.image.load(start_image).convert()
		end = pygame.image.load(end_image).convert_alpha()
		loot = pygame.image.load(loot_image).convert_alpha()

		# on parcourt la liste issue de level_generation
		line_number = 0
		for line in self.structure:
			box_number = 0
			for sprite in line:
				# on définit la position x et y en pixel pour chaque sprite
				x = box_number * sprite_size
				y = line_number * sprite_size
					# on met à jour window avec les images indiquées dans level_structure en les mettant à la bonne position
				if sprite == 'w':
					window.blit(wall, (x,y))
				elif sprite == 's':
					window.blit(start, (x,y))
				elif sprite == 'e':
					window.blit(end, (x,y))
				elif sprite == 'l':
					window.blit(loot, (x,y))
				box_number += 1
			line_number += 1


class Hero:

	def __init__(self, top, down, left, right, level):
		# attributs pour le déplacement
		self.top = pygame.image.load(top).convert_alpha()
		self.down = pygame.image.load(down).convert_alpha()
		self.left = pygame.image.load(left).convert_alpha()
		self.right = pygame.image.load(right).convert_alpha()
		# position du personnage en cases et en pixels
		self.box_x = 0
		self.box_y = 0
		self.x = 0
		self.y = 0

		self.direction = right
		self.level = level		


	def move(self, direction):

		if direction == 'right':
			if self.box_x < (number_side_sprite -1):
				if self.level.structure[self.box_y][self.self.box_x+1] != 'w':
					self.box_x += 1
					self.x = self.box_x * sprite_size
			self.direction = self.right
		
		if direction == 'left':
			if self.box_x > 0:
				if self.level.structure[self.box_y][self.box_x-1] != 'w':
					self.box_x -= 1
					self.x = self.box_x * sprite_size
			self.direction = self.left
 
		if direction == 'top':
			if self.box_y > 0:
				if self.level.structure[self.box_y-1][self.box_x] != 'w':
					self.box_y -= 1
					self.y = self.box_y * sprite_size
			self.direction = self.top

		if direction == 'down':
			if self.box_y < (number_side_sprite -1):
				if self.level.structure[self.box_y+1][self.box_x] != 'w':
					self.box_y += 1
					self.y = self.box_y * sprite_size
			self.direction = self.down
