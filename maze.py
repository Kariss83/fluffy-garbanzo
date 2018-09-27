#!/usr/bin/env python3
# coding: utf-8


import csv
import pygame

PIXELS_PER_SPRITE = 60


class Maze:
    """This class allows to read the  structure of the game lvl itself : the 
    maze from a csv file"""

    def __init__(self, data_file):
        """the data_file expected is the one containing the maze stucture
        in a csv file with ';' as delimiter"""
        self.file = data_file
        self.structure = []
        self.empty = []
        self.empty_for_obj = []
        self.entry = []
        self.exit = []
        self.items = []

    def creation(self):
        """This method will allow the reading and and use of the csv file
        in order to build and store in the attribute 'structure' the maze
        as a set of values (the one for each sprite)"""
        with open(self.file, "r") as mazestructure:
            lvl_structure = []
            reader = csv.reader(mazestructure, delimiter=';')

            for x, lines in enumerate(reader):
                line_structure = []
                for y, sprite in enumerate(lines):
                    line_structure.append(sprite)
                    if sprite == 'o':
                        self.empty.append((x, y))
                        self.empty_for_obj.append((x, y))
                    elif sprite == 'entry':
                        self.entry.append((x, y))
                    elif sprite == 'e':
                        self.exit.append((x, y))
                        self.empty.append((x, y))git
                lvl_structure.append(line_structure)
            self.structure = lvl_structure

    def display(self, window, wall_img, guardian_img):
        """This method will allow to load graphical representation of the maze
        structure that we generated with the lvl_creation method in a window"""
        # loading wall sprite
        wall = pygame.image.load(wall_img).convert()

        # loading guardian sprite
        guardian = pygame.image.load(guardian_img).convert()

        # we go through the level structure to give each position its sprite
        line_number = 0
        for ligne in self.structure:
            # On parcourt les listes de lignes
            case_number = 0
            for sprite in ligne:
                # we compute the position in pixel
                x = case_number * PIXELS_PER_SPRITE
                y = line_number * PIXELS_PER_SPRITE
                # We display wall everywhere there is a free space represented by a o in the csv file
                if sprite == 'x':  # x = wall
                    window.blit(wall, (x, y))
                # And the guardian sprite at the position that contains an e for exit
                elif sprite == 'e': # e = exit
                    window.blit(guardian, (x, y))
                case_number += 1
            line_number += 1


def main():
    maze = Maze('data/maze_structure.csv')
    maze.lvl_creation()
    print(maze.structure)
    print(maze.empty)
    print(maze.exit)
    print(maze.entry)


if __name__ == "__main__":
    main()
