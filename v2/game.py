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

# génération du niveau
level = Level("level_1")
level.level_generation()
level.show_level(window)

#génération de mcgyver
mg = Hero("images/mcgyver.png", "images/mcgyver.png", "images/mcgyver.png", "images/mcgyver.png", level)

#screen refresh
pygame.display.flip()

# main loop
run = 1
while run:
    #processor load control
    pygame.time.Clock().tick(30)

    # génération du fond
    background = pygame.image.load(background_image).convert()

    #screen refresh
    pygame.display.flip()

    for event in pygame.event.get():
            if event.type == QUIT:
                run = 0

            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    mg.movement('right')
                    print("right")
                elif event.key == K_LEFT:
                    mg.movement('left')
                    print("left")
                elif event.key == K_UP:
                    mg.movement('top')
                    print("top")
                elif event.key == K_DOWN:
                    mg.movement('down')
                    print("down")

    window.blit(background, (0,0))
    level.show_level(window)
    window.blit(mg.direction, (mg.x, mg.y))
    pygame.display.flip()

    # Fin du jeu si mcgyver arrive dans la case 'e'
    if level.structure[mg.box_y][mg.box_x] == 'e':
        run = 0

