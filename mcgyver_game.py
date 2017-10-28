#-*- code:utf8 -*-

# Définition des  dclasses indentifiées :

# une classe Hero pour créer McGyver
class Hero:

    def __init__(self, life, needle, plastic_tube, ether):
        self.life = life
        self.needle = needle
        self.plastic_tube = plastic_tube
        self.ether = ether

    # méthode de déplacement
    def move(self):
        # se déplacer vers le haut
        # se déplacer vers le bas
        # se déplacer à droite
        # se déplacer à gauche
        pass

    # méthode pour ramasser des objets
    def loot(self):
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

    def __init__(self, life):
        self.life = life

    # méthode pour se battre
    def fight(self):
        # Si Hero et Gardian sur la même position :
            # Si hero.needle = true et hero.plastic_tube = true et hero.ether = true:
                # gardian.life = 0 et gardian est détruit
            # Sinon : hero.life = 0 et fin du programme
        pass


# une classe Prison pour créer la zone de jeu
class Prison:

    PRISON_WIDTH = 15
    PRISON_HEIGHT = 15

    def __init__(self):
        self.prison_width = self.PRISON_WIDTH
        self.prison_height = self.PRISON_HEIGHT

    # initialiser les zones du jeu
    def initialize_prison_zones(self):
        pass

# une classe Loot pour créer les objets à ramasser
class Loot:

    def __init__(self, type, loot_status):
        self.type = type
        self.loot_status = loot_status


# une classe pour définir la position des objets
class Position:

    def __init_(self, width, height):
        self.width = width
        self.height = height



def main():
    # création des objets
    gardian = Gardian(100)
    prison = Prison()
    needle = Loot("needle", False)
    plastic_tube = Loot("plastic_tube", False)
    ether = Loot("ether", False)
    mcgyver = Hero(100, needle.loot_status, plastic_tube.loot_status, ether.loot_status)

    # test des objets créés
    print(gardian.life)
    print(prison)
    print(needle.type, needle.loot_status)
    print(plastic_tube.type, plastic_tube.loot_status)
    print(ether.type, ether.loot_status)
    print(mcgyver.life, mcgyver.needle, mcgyver.plastic_tube, mcgyver.ether)


main()

