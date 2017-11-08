import pygame
from pygame.locals import *
from config import *

class Hero:
    def __init__(self, top, down, left, right, level):
        # sprites haut, bad, gauche, droit pour le personnage.
        self.top = pygame.image.load(top).convert_alpha()
        self.down = pygame.image.load(down).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.right = pygame.image.load(right).convert_alpha()
        # position du personnage en cases et en pixels
        self.box_x = 0
        self.box_y = 0
        self.x = 0
        self.y = 0
        self.loot1 = False
        self.loot2 = False
        self.loot3 = False

        # direction par défaut
        self.direction = self.right
        self.level = level

    def movement(self, direction):
        # méthode de déplacement du personnage

        if direction == 'right':
            # pour ne pas dépasser l'écran :
            if self.box_x < (number_side_sprite - 1):
                # si pas un mur :
                if self.level.structure[self.box_y][self.box_x + 1] != 'w':
                    # alors x est incrémenté de 1 (= déplacement d'une case à droite)
                    self.box_x += 1
                    # conversion de la position de x en pixels par rapport à la nouvelle position de box_x
                    self.x = self.box_x * sprite_size
            # image = right
            self.direction = self.right

        if direction == 'left':
            if self.box_x > 0:
                if self.level.structure[self.box_y][self.box_x - 1] != 'w':
                    self.box_x -= 1
                    self.x = self.box_x * sprite_size
            self.direction = self.left

        if direction == 'top':
            if self.box_y > 0:
                if self.level.structure[self.box_y - 1][self.box_x] != 'w':
                    self.box_y -= 1
                    self.y = self.box_y * sprite_size
            self.direction = self.top

        if direction == 'down':
            if self.box_y < (number_side_sprite - 1):
                if self.level.structure[self.box_y + 1][self.box_x] != 'w':
                    self.box_y += 1
                    self.y = self.box_y * sprite_size
            self.direction = self.down
