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
            line_number = 0
            reader = csv.reader(mazestructure, delimiter=';')

            # -tc- for line_number, line in enumerate(reader) (pour lines au pluriel?)
            for lines in reader:
                line_structure = []
                sprite_number = 0
                # -tc- for sprite_number, sprite in enumerate(line)
                for sprite in lines:
                    line_structure.append(sprite)
                    if sprite == 'o':
                        self.empty.append((line_number, sprite_number))
                        self.empty_for_obj.append((line_number, sprite_number))
                    elif sprite == 'entry':
                        # -tc- Pourquoi self.entry est une liste? Il n'y aura jamais plus de une position
                        self.entry.append((line_number, sprite_number))
                        # -tc- Tu as oublié d'ajouter la position de entry à ta liste, ce qui introduit un bug
                        # -tc- dans ton jeu
                        self.empty.append((line_number, sprite_number))
                    elif sprite == 'e':
                        # -tc- Pourquoi self.exit est une liste? Il n'y aura jamais plus de une position
                        self.exit.append((line_number, sprite_number))
                        self.empty.append((line_number, sprite_number))
                    # -tc- Pas nécessaire avec enumerate qui est la manière idiomatique de faire
                    sprite_number += 1
                line_number += 1
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
        # -tc- ou for line_number, line in enumerate(self.structure)
        # -tc- Pourquoi ligne est en français?
        for ligne in self.structure:
            # On parcourt les listes de lignes
            case_number = 0
            # -tc- for case_number, sprite in enumerate(line)
            for sprite in ligne:
                # we compute the position in pixel
                x = case_number * PIXELS_PER_SPRITE
                y = line_number * PIXELS_PER_SPRITE
                if sprite == 'x':  # x = wall
                    window.blit(wall, (x, y))
                elif sprite == 'e':
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
