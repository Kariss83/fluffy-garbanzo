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

    def lvl_creation(self):
        """This method will allow the reading and and use of the csv file
        in order to build and store in the attribute 'structure' the maze 
        as a set of values (the one for each sprite)"""
        with open(self.file, "r") as mazestructure:
            lvl_structure = []
            reader = csv.reader(mazestructure, delimiter=';')
            for lines in reader:
                line_structure = []
                for sprite in lines:
                    line_structure.append(sprite)
                lvl_structure.append(line_structure)
            self.stucture = lvl_structure


def main():
    maze = Maze('data/maze_structure.csv')
    maze.lvl_creation()

        
if __name__ == "__main__":
    main()
