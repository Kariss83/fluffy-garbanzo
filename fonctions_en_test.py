#! usr/bin/env/python3
# coding: utf-8


import random
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
                    sprite_number += 1
                lvl_structure.append(line_structure)
                line_number += 1
            self.stucture = lvl_structure

    def lvl_display(self):
        """This method will allow to load graphical representation of the maze
        structure that we generated with the lvl_creation method in a window"""
        #associer à chaque lettre une image
        #parcourir self.structure pour associer à chaque sprite une immage

class Item:
    """This class will allow the creation of any item that lies on the game
    structure (object or NPC)"""
    
    def __init__(self, lvl, sprite):
        self.case_x = 0
        self.case_y = 0
        self.sprite = sprite
        self.level = lvl

    def placing_items(self, lvl):

        random.seed()
        k = random.randint(0, len(lvl.empty) -1)
        self.case_x = lvl.empty[k][0]
        self.case_y = lvl.empty[k][1]
        del(lvl.empty[k])

		
def main():
	maze = Maze('data/maze_structure.csv')
	maze.lvl_creation()
	print(maze.structure)
	print(maze.empty)
	seringue = Item(maze, 0)
	print(seringue.case_x, seringue.case_y)
	seringue.placing_items(maze)
	print(maze.empty)
	print(seringue.case_x, seringue.case_y)
	liquide = Item(maze, 1)
	liquide.placing_items(maze)
	print(maze.empty)
	

        
if __name__ == "__main__":
    main()

