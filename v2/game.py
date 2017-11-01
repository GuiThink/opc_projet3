#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *

from classes import *
from constantes import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
window = pygame.display.set_mode((window_side, window_side))
icon = pygame.image.load(icon_image)
pygame.display.set_icon(icon)
#Titre
pygame.display.set_caption(window_title)


# main loop
run = 1
while run:

    #processor load control
    pygame.time.Clock().tick(30)

    #screen refresh
    pygame.display.flip()

    for event in pygame.event.get():
            if event.type == QUIT:
                run = 0

    # génération du fond
    background = pygame.image.load(background_image).convert()

    # génération du niveau
    level = Level("level_1")
    level.level_generation()
    level.show_level(window)

    #génération de mcgyver
    mg = Hero("images/mcgyver.png", "images/mcgyver.png", "images/mcgyver.png", "images/mcgyver.png", level)

    window.blit(background, (0,0))
    level.show_level(window)
    # ne marche pas :
    #window.blit(mg.direction, (mg.x, mg.y))
    pygame.display.flip()

