#!/usr/bin/env python3
# coding: utf-8


import csv


class Maze:
    """This class allows to read the  structure of the game lvl itself : the 
    maze from a csv file"""

    def __init__(self, data_file): 
        """the data_file expected is the one containing the maze stucture
        in a csv file with ';' as delimiter"""
        self.file = data_file
        self.structure = []
        self.empty = []

    # -tc- pourquoi pas simplement creation (on est déjà dans une classe représentant le labyrinthe?
    def lvl_creation(self):
        """This method will allow the reading and and use of the csv file
        in order to build and store in the attribute 'structure' the maze 
        as a set of values (the one for each sprite)"""
        with open(self.file, "r") as mazestructure:
            lvl_structure = []
            line_number = 0
            reader = csv.reader(mazestructure, delimiter=';')
            # -tc- plutôt que de maintenir les variables line_number et sprite_number
            # -tc- à la main, la aolution pythonique est plutôt d'utiliser enumerate()
            for lines in reader:
                line_structure = []
                sprite_number = 0
                for sprite in lines:
                    line_structure.append(sprite)
                    if sprite == 'o':
                        self.empty.append((line_number,sprite_number))
                        # -tc- Il peut être avantageux d'utiliser un ensemble plutot qu'une liste
                    sprite_number += 1
                lvl_structure.append(line_structure)
                line_number += 1
            self.stucture = lvl_structure
            

    # -tc- Pourquoi pas simplement display ?
    # -tc- Dans un soucis de représentation des couches, la représentation graphique
    # -tc- du labyrinthe ne devrait pas être la préoccupation de Maze
    def lvl_display(self):
        """This method will allow to load graphical representation of the maze
        structure that we generated with the lvl_creation method in a window"""
        #associer à chaque lettre une image
        #parcourir self.structure pour associer à chaque sprite une immage



def main():
    maze = Maze('data/maze_structure.csv')
    maze.lvl_creation()
    print(maze.empty)

        
if __name__ == "__main__":
    main()
