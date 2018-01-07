#! /usr/bin/env python3
# coding: utf-8
"""This class generates maze, hero, badguy
as well as random loots"""
import pygame
from pygame.locals import *
import random

# game images
BACKGROUND_IMAGE = "images/background.png"
START_IMAGE = "images/start.png"
END_IMAGE = "images/end.png"
WALL_IMAGE = "images/wall.png"
LOOT_IMAGE = "images/loot.png"
HERO_IMAGE = "images/mcgyver.png"


class Level(object):
    """Class generates the maze and hero, badguy position.
    Moreover, it generates random loots positions"""
    def __init__(self, file):
        self.file = file
        self.structure = []
        self.level_generation()
        self.generate_loot('l')
        self.generate_loot('m')
        self.generate_loot('n')
        self.loot_list = []

    def level_generation(self):
        """Generate a maze based on a file and append it in a list."""
        with open(self.file, "r") as file:
            for line in file:
                level_line = []
                for sprite in line:
                    if sprite != '\n' and sprite != ';':
                        level_line.append(sprite)
                self.structure.append(level_line)

    def generate_loot(self, loot_name):
        """Calls function random_loot
        and then attribuates coords [x][y] of the structure to the loot in parameters
        depending on the result of the function random_loot."""
        [x, y] = self.random_loot()
        self.structure[x][y] = loot_name

    def random_loot(self):
        """Determines a random x and y between 0 and 14 (0 included).
        and creates a variable coord_valids that calls the function is_case_empty
        to check if the random coords correspond to an empty case."""
        coord_valids = False
        x = 0
        y = 0
        while coord_valids is False:
            x = random.randrange(0, 15)
            y = random.randrange(0, 15)
            coord_valids = self.is_case_empty(x, y)
        return [x, y]

    def is_case_empty(self, x, y):
        """Checks if structure[x][y] corresponds to an empty cell or not.
        if the cell is empty it returns true and the while-loop in random_loot ends.
        The x and y coords are then attribuated to the loot variable in generate_loot function."""
        return self.structure[x][y] == ' '

    def set_hero_position(self, x, y):
        """Takes an x and y in parameters and attribuate 'M'
        to these coords in the Maze (= prints Hero)
        Params come from x, y initiated for the instance of the Hero class.
        """
        self.structure[x][y] = 'M'

    def is_lootable(self, x, y):
        """Verifies if structure[x][y] contains a loot. If True, calls function get_loot()"""
        if self.structure[x][y] in ['l', 'm', 'n']:
            self.get_loot()
        else:
            pass

    def get_loot(self):
        """Adds a mention 'loot' to the loot list which permits
        to verify that the 3 loots of the maze have been loot.
        Then calls function loot_list_check() to verify if all
        loots are grabed by Hero"""
        loot = 'loot'
        self.loot_list.append(loot)
        self.loot_list_check()

    def loot_list_check(self):
        """if Loot list has all 3 items, then we consider hero
        to be available to espace the maze : returns True"""
        loot_list = len(self.loot_list)
        if loot_list == 3:
            return True
        else:
            return False

    def is_case_valid(self, x, y):
        """Checks the position of the hero to allow him to change cell or not
        depending on if the cell is a wall.
        If hero is not out of range and the cell is not a wall it returns back True
        to the move function. Move function then allow the hero to move accordingly."""
        if x >= 0 and x < 15 and y >= 0 and y < 15 and self.structure[x][y] != "#":
            return True

    def clear_cell(self, x, y):
        """
        Clears the cell by puting it at ' ' value. Used to clear 'M'
        from the maze once the hero has moved from its original position."""
        if self.structure[x][y] == self.structure[0][0]:
            self.structure[0][0] = 's'
        else:
            self.structure[x][y] = ' '

    def show_level(self, window):
        """Function generates maze images"""
        background = pygame.image.load(BACKGROUND_IMAGE).convert()
        wall = pygame.image.load(WALL_IMAGE).convert()
        start = pygame.image.load(START_IMAGE).convert()
        end = pygame.image.load(END_IMAGE).convert_alpha()
        loot = pygame.image.load(LOOT_IMAGE).convert_alpha()
        hero = pygame.image.load(HERO_IMAGE).convert_alpha()

        window.blit(background, (0, 0))
        window.blit(start, (0, 0))
        line_number = 0

        for line in self.structure:
            box_number = 0
            for sprite in line:
                x = box_number * 30
                y = line_number * 30

                if sprite == '#':
                    window.blit(wall, (x, y))
                elif sprite == 'e':
                    window.blit(end, (x, y))
                elif sprite == 'l':
                    window.blit(loot, (x, y))
                elif sprite == 'm':
                    window.blit(loot, (x, y))
                elif sprite == 'n':
                    window.blit(loot, (x, y))
                elif sprite == 'M':
                    window.blit(hero, (x, y))

                box_number += 1
            line_number += 1
