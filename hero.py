#! /usr/bin/env python3
# coding: utf-8
"""Generates hero and lose or win conditions"""
import pygame
from pygame.locals import *
from level import *


class Hero(object):
    """Class generates hero as well has its position
    and win or lose state"""
    def __init__(self, level):
        self.x = 0
        self.y = 0
        self.level = level
        # generate the maze as a param of the Hero class
        # (means the maze is generated once the instance of the hero class is initiated)
        self.level.set_hero_position(self.x, self.y)
        # calls and sets x, y coords as params of the function set_hero_position (defaults to 0,0)

    def move(self, direction):
        """
        attribuates x, y coords to the hero depending on they direction
        typed for get_direction function and x, y resulting of get_new_coords function.
        Calls function check_move to verify that coords are valid and allow a move.
        Then, it clears the current cell and moves hero to the new coords.
        """
        self.direction = direction
        y, x = self.get_new_coords(self.get_direction(direction)) # go gets w, y coords
        if self.level.is_case_valid(x, y): # checks if allowed to go to new cell
            self.level.clear_cell(self.x, self.y) # clears the cell
            self.x = x # add x to self.x
            self.y = y # add y to self.y
        self.level.is_lootable(self.x, self.y)
        fight = self.fight(self.x, self.y)
        self.level.set_hero_position(self.x, self.y)
        # finally attribuated x and y coords to the hero that can then be printed
        return fight

    def get_direction(self, direction):
        """Input in the terminal to get the direction requested by user.
        If nothing type = no move."""
        # direction = input('Direction >')
        if self.direction == 'z':
            return 'TOP'
        elif self.direction == 's':
            return 'DOWN'
        elif self.direction == 'd':
            return 'RIGHT'
        elif self.direction == 'q':
            return 'LEFT'
        else:
            return ''

    def get_new_coords(self, direction):
        """
        Takes direction from function get_direction as a param
        to define the new x, y coords to be attribuated to the Hero.
        """
        if direction == 'TOP':
            return [self.y, self.x - 1] # returns news x, y coords
        elif direction == 'DOWN':
            return [self.y, self.x + 1]
        elif direction == 'RIGHT':
            return [self.y + 1, self.x]
        elif direction == 'LEFT':
            return [self.y - 1, self.x]
        else:
            return [self.y, self.x]
            # if direction not top, down, right, left = position stays at current state

    def fight(self, x, y):
        """If hero on the last cell of the maze, function fight()
        verifies that hero has 3 loots. If True, the hero wins."""
        if self.level.structure[x][y] == 'e':
            if self.level.loot_list_check():
                return True
            else:
                return True
        else:
            return False
