#-*- code:utf8 -*-

# Définition des 4 classes indentifiées :

# une classe Hero pour créer McGyver
class Hero:

    def __init__(self, life):
        self.life = life

# une classe Gardian pour créer le méchant
class Gardian:

    def __init__(self, life):
        self.life = life


# une classe Prison pour créer la zone de jeu
class Prison:

    PRISON_WIDTH = 15
    PRISON_HEIGHT = 15

    def __init__(self):
        self.prison_width = self.PRISON_WIDTH
        self.prison_height = self.PRISON_HEIGHT

# une classe Loot pour créer les objets à ramasser
class Loot:

    def __init__(self, type, loot_status):
        self.type = type
        self.loot_status = loot_status



def main():
    # création des objets
    mcgyver = Hero(100)
    gardian = Gardian(100)
    prison = Prison()
    needle = Loot("needle", False)
    plastic_tube = Loot("plastic_tube", False)
    ether = Loot("ether", False)

    # test des objets créés
    print(mcgyver.life)
    print(gardian.life)
    print(prison)
    print(needle.type, needle.loot_status)
    print(plastic_tube.type, plastic_tube.loot_status)
    print(ether.type, ether.loot_status)

main()

