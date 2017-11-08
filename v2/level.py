import pygame
from pygame.locals import *
from random import randrange
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


## tests pour générer les loots aléatoirement...euh...je suis perdu.

    # def random_loot(self):
    #     loot = pygame.image.load(loot_image).convert_alpha()
    #     self.x = 0
    #     self.y = 0
    #     self.rand_x = random.randint()
    #
    #
    #     # on créé une structure uniquement pour les loots et basée sur le contenu de self.structure
    #     loot_structure = []
    #     # on parcourt la structure du niveau
    #     for line in self.structure:
    #         # pour chaque ligne, on vérifie que la valeur du sprite n'est pas w, ou s, ou e
    #         loot_line = []
    #         for sprite in line:
    #             if sprite != 'w' or 's' or 'e'or '\n' :
    #                 # si la condition est vérifiée :
    #                 loot_line.append(True)

    # def rand_loot(self):
    #     loot_x = 0
    #     loot_y = 0
    #
    #     for line in self.structure:
    #         for sprite in line:
    #             if sprite == ' ':
    #                 ss

    # foo = ['a', 'b', 'c', 'd', 'e']
    # # from random import randrange
    # random_index = randrange(0,len(foo))
    # print foo[random_index]
    #
    #
    # while sprite != 'w' or 's' or 'e':
    #     rand_x = randrange(level_line)
    #     rand_y = randrange()


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
                # elif sprite == 'l':
                #     window.blit(loot, (x, y))
                box_number += 1
            line_number += 1