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
        self.entry = []
        self.exit = []
        self.items = []

    @property
    def empty_for_obj(self):
        return self.empty
        
        
        
    def lvl_creation(self):
        """This method will allow the reading and and use of the csv file
        in order to build and store in the attribute 'structure' the maze 
        as a set of values (the one for each sprite)"""
        with open(self.file, "r") as mazestructure:
            lvl_structure = []
            line_number = 0
            reader = csv.reader(mazestructure, delimiter=';')
            
            for lines in reader:
                line_structure = []
                sprite_number = 0
                
                for sprite in lines:
                    line_structure.append(sprite)
                    if sprite == 'o':
                        self.empty.append((line_number,sprite_number))
                    elif sprite == 'entry':
                        self.entry.append((line_number, sprite_number))
                    elif sprite == 'exit':
                        self.exit.append((line_number, sprite_number))
                    sprite_number += 1                
                line_number += 1
                lvl_structure.append(line_structure)
            self.structure = lvl_structure

            
    
    def lvl_display(self):
        """This method will allow to load graphical representation of the maze
        structure that we generated with the lvl_creation method in a window"""
        #associer à chaque lettre une image
        #parcourir self.structure pour associer à chaque sprite une image
    
    
def main():
    maze = Maze('data/maze_structure.csv')
    maze.lvl_creation()
    print(maze.structure)
    print(maze.empty)
    print(maze.exit)
    print(maze.entry)

        
if __name__ == "__main__":
    main()