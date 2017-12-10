import random
import pygame
from pygame.locals import *


# game images
background_image = "images/background.png"
start_image = "images/start.png"
end_image = "images/end.png"
wall_image = "images/wall.png"
loot_image = "images/loot.png"
hero_image = "images/mcgyver.png"

#window parameters
number_side_sprite = 15
sprite_size = 30
window_side = number_side_sprite * sprite_size

# game title
window_title = "Sauvez McGyver !!!"
icon_image = "images/mcgyver.png"



class Level:
    def __init__(self, file):
        self.file = file # maze file
        self.structure = [] # maze
        self.level_generation() # calls level_generation during the init
        self.generate_loot('l') # calls function generate_loot with 'l' as parameter during the init
        self.generate_loot('m')
        self.generate_loot('n')
        self.inventory = []


    def level_generation(self):
        """Generate a maze based on a file and append it in a list."""
        with open(self.file, "r") as file:
            for line in file:
                level_line = []
                for sprite in line:
                    if sprite != '\n' and sprite != ';':
                        level_line.append(sprite)
                self.structure.append(level_line)

    # for testing purpose only :
    def print_level(self):
        """Print the maze for testing purpose in terminal"""
        for line in self.structure:
            print("".join(line))


    def generate_loot(self, loot_name):
        """Calls function random_loot
        and then attribuates coords [x][y] of the structure to the loot in parameters
        depending on the result of the function random_loot."""
        [x, y] = self.random_loot() # calls function random_loot for [x, y] attribution
        self.structure[x][y] = loot_name # l, m, n get a position in the structure based on the x and y values returned back by random_loot function


    def random_loot(self):
        """Determines a random x and y between 0 and 14 (0 included).
        and creates a variable coord_valids that calls the function is_case_empty
        to check if the random coords correspond to an empty case."""
        coord_valids = False
        x = 0
        y = 0
        while coord_valids == False: # while-loop that stops with the condition that structure.[y][x] is an empty cell.
            x = random.randrange(0, 15)
            y = random.randrange(0, 15)
            coord_valids = self.is_case_empty(x, y) # calls is_case_empty to verify is the cell is empty or not.
        # print("%d" % x) # print x for checking purpose
        # print("%d" % y) # print y for checking purpose
        return [x, y] # returns [x, y] so it is attribuated back to the loot_name in the generate_loot function.


    def is_case_empty(self, x, y):
        """Checks if structure[x][y] corresponds to an empty cell or not.
        if the cell is empty it returns true and the while-loop in random_loot ends.
        The x and y coords are then attribuated to the loot variable in generate_loot function."""
        if self.structure[x][y] == ' ':
            return True
        else:
            return False


    def set_hero_position(self, x, y):
        """Takes an x and y in parameters and attribuate 'M' to these coords in the Maze (= prints Hero)
        Params come from x, y initiated for the instance of the Hero class.
        """
        self.structure[x][y] = 'M'


    def check_move(self, x, y):
        """Verifies that coords put in parameters are valid or not (= in range && != "#") and returns True or False.
        Params come from :
        """
        if self.is_case_valid(x, y):
            return True
        else:
            return False


    def is_lootable(self, x, y):
        if self.structure[x][y] == 'l' or self.structure[x][y] == 'm' or self.structure[x][y] == 'n':
            print("There is a loot !!! I grab it ;)")
            self.get_loot()
        else:
            print("No loot here.")


    def get_loot(self):
        loot = 'loot'
        self.inventory.append(loot)
        self.inventory_check()
        print(self.inventory)


    def inventory_check(self):
        inventory = len(self.inventory)
        if inventory == 3:
            print("Yeah, I got 3 items in my inventory. Ready for a fight !")
            return True
        else:
            print("Yiiiks !!! need some more stuff !")
            return False


    def is_case_valid(self, x, y):
        """Checks the position of the hero to allow him to change cell or not
        depending on if the cell is a wall.
        If hero is not out of range and the cell is not a wall it returns back True
        to the move function. Move function then allow the hero to move accordingly."""
        if x >= 0 and x < 15 and y >= 0 and y < 15 and self.structure[x][y] != "#":
            return True
        else:
            return False


    def clear_cell(self, x, y):
        """
        Clears the cell by puting it at ' ' value. Used to clear 'M' from the maze once the hero has moved from its original position."""
        if self.structure[x][y] == self.structure[0][0]:
            self.structure[0][0] = 's'
        else: self.structure[x][y] = ' '


    def show_level(self, window):
        background = pygame.image.load(background_image).convert()
        wall = pygame.image.load(wall_image).convert()
        start = pygame.image.load(start_image).convert()
        end = pygame.image.load(end_image).convert_alpha()
        loot = pygame.image.load(loot_image).convert_alpha()
        hero = pygame.image.load(hero_image).convert_alpha()
        # on parcourt la liste issue de level_generation
        window.blit(background, (0, 0))
        window.blit(start, (0, 0))
        line_number = 0
        for line in self.structure:
            box_number = 0
            for sprite in line:
                # on définit la position x et y en pixel pour chaque sprite
                x = box_number * 30
                y = line_number * 30
                # on met à jour window avec les images indiquées dans level_structure en les mettant à la bonne position
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
                # elif sprite == ' ':
                #     window.blit(background, (x, y))
                box_number += 1
            line_number += 1


class Hero():
    def __init__(self, level):
        self.x = 0
        self.y = 0
        self.level = level # generate the maze as a param of the Hero class (means the maze is generated once the instance of the hero class is initiated)
        self.level.set_hero_position(self.x, self.y) # calls and sets x, y coords as params of the function set_hero_position (defaults to 0,0)


    def move(self, direction):
        """
        attribuates x, y coords to the hero depending on they direction typed for get_direction function and x, y resulting of get_new_coords function.
        Calls function check_move to verify that coords are valid and allow a move. Then, it clears the current cell and moves hero to the new coords.
        """
        self.direction = direction
        y, x = self.get_new_coords(self.get_direction(direction)) # go gets w, y coords
        if self.level.check_move(x, y): # checks if allowed to go to new cell
            self.level.clear_cell(self.x, self.y) # clears the cell
            self.x = x # add x to self.x
            self.y = y # add y to self.y
        self.level.is_lootable(self.x, self.y)
        self.fight(self.x, self.y)
        self.level.set_hero_position(self.x, self.y) # finally attribuated x and y coords to the hero that can then be printed
        self.level.print_level() # prints the maze for verification purpose


    def get_direction(self, direction):
        """Input in the terminal to get the direction requested by user. If nothing type = no move."""

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
        Takes direction from function get_direction as a param to define the new x, y coords to be attribuated to the Hero.
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
            return [self.y, self.x] # if direction not top, down, right, left = position stays at current state


    def fight(self, x, y):
        if self.level.structure[x][y] == 'e':
            if self.level.inventory_check():
                print("You won !!! McGyver escapes away from this crazy maze.")
                exit()
            else:
                print("You die miserably...")
                exit()
        else:
            pass


def main():
    level = Level("level_1") # generates maze instance base on level_1 file
    mcgyver = Hero(level) # generates hero instance
    window = pygame.display.set_mode((window_side, window_side)) # generates the game window
    pygame.display.set_caption(window_title) # set title
    level.show_level(window)  # Level generation in pygame
    pygame.display.flip() #screen refresh
    key = ''

    run = True
    while run == True: # game loop

        pygame.init()

        pygame.time.Clock().tick(30) #processor load control

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            elif event.type == KEYDOWN:
                if event.key == K_d:
                    key = 'd'
                elif event.key == K_q:
                    key = 'q'
                elif event.key == K_z:
                    key = 'z'
                elif event.key == K_s:
                    key = 's'
                mcgyver.move(key)


        level.show_level(window)
        pygame.display.flip()


if __name__ == '__main__':
    main()
