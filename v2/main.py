#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *
from hero import Hero
from level import Level
from config import *


def main():

    pygame.init()

    #Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
    window = pygame.display.set_mode((window_side, window_side))
    icon = pygame.image.load(icon_image)
    pygame.display.set_icon(icon)
    #Titre
    pygame.display.set_caption(window_title)

    # génération du niveau
    level = Level("level_1")
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
        background = pygame.image.load("images/background.png").convert()

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
        #window.blit(loot1.random_position(), (loot1.x, loot1.y))
        window.blit(mg.direction, (mg.x, mg.y))
        pygame.display.flip()

        # Loot d'un objet
        # if level.structure[mg.box_y][mg.box_x] == level.structure['l']:
        #     mg.loot1 == True


        # Fin du jeu si mcgyver arrive dans la case 'e' et qu'il a tous les loot
        if level.structure[mg.box_y][mg.box_x] == 'e'and mg.loot1 == True and mg.loot2 == True and mg.loot3 == True:
            run = 0


if __name__ == '__main__':
    main()