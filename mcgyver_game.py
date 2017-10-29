#-*- code:utf8 -*-

import random
import json

# Définition des  dclasses indentifiées :

# une classe Hero pour créer McGyver
class Hero:

    def __init__(self, **hero_list):
        for attr_name, attr_value in hero_list.items():
            setattr(self, attr_name, attr_value)

    # méthode de déplacement
    def move(self):
        # se déplacer vers le haut
        # se déplacer vers le bas
        # se déplacer à droite
        # se déplacer à gauche
        pass

    # méthode pour ramasser des objets
    def loot_item(self):
        # si Hero sur la même position que Loot alors Loot_status = true
        pass

    # méthode pour sortir de la prison
    def leave_prison(self):
        # tant que gardian.life != 0 et hero position != position exit_door :
            #pass
        # Sinon fin du programme
        pass


# une classe Gardian pour créer le méchant
class Gardian:

    def __init__(self, **gardian_list):
        for attr_name, attr_value in gardian_list.items():
            setattr(self, attr_name, attr_value)

    # méthode pour se battre
    def fight(self):
        # Si Hero et Gardian sur la même position :
            # Si hero.needle = true et hero.plastic_tube = true et hero.ether = true:
                # gardian.life = 0 et gardian est détruit
            # Sinon : hero.life = 0 et fin du programme
        pass


# une classe Loot pour créer les objets à ramasser
class Loot:

    def __init__(self, **loot_list):
        for attr_name, attr_value in loot_list.items():
            setattr(self, attr_name, attr_value)


# une classe pour définir la position des objets
class Position:

    def __init_(self):
        self.longitude = random.randint(0, 15)
        self.latitude = random.randint(0.15)


class Zone:

    MIN_LONGITUDE = 0
    MAX_LONGITUDE = 15
    WIDTH = 1

    def __init__(self, corner1, corner2):
        self.corner1 = corner1
        self.corner2 = corner2

    def initialize_zones(self):
        for longitude in range(self.MIN_LONGITUDE, self.MAX_LONGITUDE, self.WIDTH):
            bottom_left_corner = Position(longitude, 1)
            top_right_corner = Position(longitude + self.WIDTH)
            zone = Zone(bottom_left_corner)


def main():
    # création des objets

    for loot in json.load(open("loot_list.json")):
        loot = Loot(**loot)
        print(loot.loot_type, loot.loot_status, loot.position)

    for hero in json.load(open("hero_list.json")):
        hero = Hero(**hero)
        print(hero.name, hero.life, hero.position)

    for gardian in json.load(open("gardian_list.json")):
        gardian = Gardian(**gardian)
        print(gardian.name, gardian.life, gardian.position)


main()

