"""
Jeu McGyver
Déplacez vous dans le labyrinthe où est enfermé McGyver. Récupérez l'aiguille, le tube en plastique, l'éther...et foncez endormir votre ravisseur pour sortir de cette prison !

Script Python
Fichiers : mcgyver.py, classes.py, constantes.py, niveau_1 + images

"""

import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((640, 480), RESIZABLE)

#icon = pygame.image.load(image_icon)
#pygame.dispplay.set_icon(icon)

pygame.display.set_caption("Sauvez McGyver !")

# chargement de l'image de fond
background = pygame.image.load("background.jpg").convert()
# superposition de l'image de fond sur la fenêtre de jeu à partir de x=0 et y=0
window.blit(background, (0,0))

# chargement et collage de mcgyver + gestion png avec convert_aplha
hero = pygame.image.load("mcgyver.png").convert_alpha()
# fonction rect pour gérer le mouvement des rectanbles (personnages)
position_hero = hero.get_rect()
window.blit(hero, position_hero)

# chargement et collage du méchant + gestion png avec convert_alpha
badguy = pygame.image.load("badguy.png").convert_alpha()
window.blit(badguy, (300,200))

# update de l'affichage
pygame.display.flip()

# boucle pour laisser la fenêtre ouverte
run = 1

while run:
	for event in pygame.event.get(): #On parcours la liste de tous les events reçus
		if event.type == QUIT: #Si event de type QUIT on arrête la boucle
			run = 0
		if event.type == KEYDOWN: #Collecte des événements du clavier
			if event.key == K_s:
				position_hero = position_hero.move(0,15)
			if event.key == K_z:
				position_hero = position_hero.move(0,-15)	
			if event.key == K_q:
				position_hero = position_hero.move(-15,0)
			if event.key == K_d:
				position_hero = position_hero.move(15,0)
	
	# Recollage
	window.blit(background, (0,0))
	window.blit(hero, position_hero)
	# Refresh
	pygame.display.flip()
		

