import pygame
from pygame.locals import *
import random
from config import *

# game images
background_image = "images/background.png"
start_image = "images/start.png"
end_image = "images/end.png"
wall_image = "images/wall.png"
loot_image = "images/loot.png"
hero_image = "images/mcgyver.png"

class Level:
    def __init__(self, file):
        self.file = file
        self.structure = 0
        self.random_x = 0
        self.random_y = 0
        self.level_generation()
        self.generate_loot('l')
        self.generate_loot('m')
        self.generate_loot('n')

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


    def generate_loot(self, loot_name):
        x, y = self.random_loot()
        self.structure[y][x] = loot_name


    def random_loot(self):
        coord_valids = False
        x = 0
        y = 0
        while coord_valids == False:
            x = random.randrange(0, 14)
            y = random.randrange(0, 14)
            coord_valids = self.is_case_empty(x, y)
        # print("%d" % x)
        # print("%d" % y)
        # exit()
        return [x, y]


    def is_case_empty(self, x, y):
        if self.structure[y][x] == ' ':
            return True
        else:
            return False


    def show_level(self, window):
        wall = pygame.image.load(wall_image).convert()
        start = pygame.image.load(start_image).convert()
        end = pygame.image.load(end_image).convert_alpha()
        loot = pygame.image.load(loot_image).convert_alpha()
        hero = pygame.image.load(hero_image).convert_alpha()
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
                    window.blit(wall, (x, y))
                elif sprite == 's':
                    window.blit(start, (x, y))
                elif sprite == 'e':
                    window.blit(end, (x, y))
                elif sprite == 'l':
                    window.blit(loot, (x, y))
                box_number += 1
            line_number += 1
