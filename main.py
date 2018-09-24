#! usr/bin/env/python3
# coding: utf-8

# -tc- Eviter d'importer tous les symboles d'un module
from maze import * 
from items import *

		
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

