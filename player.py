#! usr/bin/env python3
# -*- coding: utf-8 -*-


# -tc- Mauvaise pratique à éviter
from maze import *
from items import *

PIXELS_PER_SPRITE = 60


class Player:
    """This class will allow the creation of the playable character
    (aka. Chuck) and allow him to move through the maze"""

    def __init__(self, sprite, lvl):
        # we load the sprite of the playable character with pygame
        # self.sprite = pygame.image.load(sprite).convert()
        # we need to indicate the lvl in order to get the initial position
        self.level = lvl
        self.sprite = pygame.image.load(sprite).convert_alpha()
        # in a particular lvl we have to look for the coordinates of the entrance
        # should be able to get a tuple with its position in the maze structure
        # -tc- ou plus pythonique: self.case_x,  self.case_y = lvl.entry[0]
        self.case_x = lvl.entry[0][0]
        self.case_y = lvl.entry[0][1]
        # inventory is empty at creation
        self.inventory = 0

    # -tc- On peut également utiliser une property plutôt que plusieurs attributs
    # -tc- qui véhiculent la même info.
    # -tc- Ca permet de corriger quelques bugs suptiles qui font apparaître des objets
    # -tc- sur des murs par exemple
    @property
    def x(self):
        return self.case_y * PIXELS_PER_SPRITE

    @property
    def y(self):
        return self.case_x * PIXELS_PER_SPRITE

    # -tc- Utiliser self.level à l'intérieur de move_to. Le paramètre lvl est par conséquent inutile
    def move_to(self, direction,  lvl):
        """Method that allow to move the player in any direction"""

        # to the right
        if direction == "right":
            # -tc- Faire attention que self.level.empty inclue self.entry[0]
            if (self.case_x, self.case_y + 1) in self.level.empty:
                # -tc- Pratique à mon avis à banir. On ne doit pas accéder à une structure de données
                # -tc- comme self.level.structure directement depuis Player. Créer une méthode
                # -tc- de toute manière inutile lvl.structure[self.case_x][self.case_y] = '0'
                self.case_y += 1

        if direction == "left":
            if (self.case_x, self.case_y - 1) in self.level.empty:
                # -tc- A éviter
                # -tc- de toute manière inutile lvl.structure[self.case_x][self.case_y] = '0'
                self.case_y -= 1

        if direction == "up":
            if (self.case_x - 1, self.case_y) in self.level.empty:
                # -tc- de toute manière inutile lvl.structure[self.case_x][self.case_y] = '0'
                self.case_x -= 1

        if direction == "down":
            if (self.case_x + 1, self.case_y) in self.level.empty:
                # -tc- de toute manière inutile lvl.structure[self.case_y][self.case_x] = '0'
                self.case_x += 1

    # -tc- Pourquoi cette méthode commence par une majuscule?
    def Pickup(self, lvl):
        if (self.case_x, self.case_y) in lvl.items:
            # -tc- Utilise logging plutôt que print
            print("vous etes sur un item, vous le ramassez ! ")
            self.inventory += 1
            lvl.items.remove((self.case_x, self.case_y))



def main():
    maze = Maze('data/maze_structure.csv')
    maze.lvl_creation()
    chuck = Player(0, maze)


if __name__ == "__main__":
    main()
