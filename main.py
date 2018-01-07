#! /usr/bin/env python3
# coding: utf-8
"""Init classes and manages loop game"""
import pygame
from pygame.locals import *
from level import *
from hero import *

#window parameters
NUMBER_SIDE_SPRITE = 15
SPRITE_SIZE = 30
WINDOW_SIDE = NUMBER_SIDE_SPRITE * SPRITE_SIZE

# game title
WINDOW_TITLE = "Sauvez McGyver !!!"

def manage_event(mcgyver):
    """pygame.event manages to record players actions on keyboard (hero moves)"""
    for event in pygame.event.get():
        if event.type == QUIT:
            return True
        elif event.type == KEYDOWN:
            key = None
            if event.key == K_d:
                key = 'd'
            elif event.key == K_q:
                key = 'q'
            elif event.key == K_z:
                key = 'z'
            elif event.key == K_s:
                key = 's'
            if key != None:
                return mcgyver.move(key)
    return False

def main():
    """Generates class and manages loop game"""
    level = Level("level_1") # generates maze instance base on level_1 file
    mcgyver = Hero(level) # generates hero instance
    window = pygame.display.set_mode((WINDOW_SIDE, WINDOW_SIDE)) # generates the game window
    pygame.display.set_caption(WINDOW_TITLE) # set title
    level.show_level(window)  # Level generation in pygame
    pygame.display.flip() #screen refresh
    key = ''

    stop = False
    while stop == False: # game loop

        pygame.init()

        pygame.time.Clock().tick(30) #processor load control

        stop = manage_event(mcgyver)
        level.show_level(window)
        pygame.display.flip()


if __name__ == '__main__':
    main()
