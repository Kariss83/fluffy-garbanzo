#!/usr/bin/env python3
# coding: utf-8


import csv
import pygame

PIXELS_PER_SPRITE = 120


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
                        self.empty_for_obj.append((line_number,sprite_number))
                    elif sprite == 'entry':
                        self.entry.append((line_number, sprite_number))
                    elif sprite == 'exit':
                        self.exit.append((line_number, sprite_number))
                        self.empty.append((line_number, sprite_number))
                    sprite_number += 1                
                line_number += 1
                lvl_structure.append(line_structure)
            self.structure = lvl_structure


    def lvl_display(self, window, wall_img, guardian_img):
        """This method will allow to load graphical representation of the maze
        structure that we generated with the lvl_creation method in a window"""
        #associer à chaque lettre une image
        #parcourir self.structure pour associer à chaque sprite une image
        #chargement des images des murs
        wall = pygame.image.load(wall_img).convert()
        
        #chargement de l'image de la sortie
        exit = pygame.image.load(guardian_img).convert()
        
        #we go through the level structure to give each position its sprite
        line_number = 0
        for ligne in self.structure:
			#On parcourt les listes de lignes
            case_number = 0
            for sprite in ligne:
				#we compute the position in pixel
                x = case_number * PIXELS_PER_SPRITE
                y = line_number * PIXELS_PER_SPRITE
                if sprite == 'x':		   #x = wall
                    window.blit(wall, (x,y))
                elif sprite == 'exit':		   
                    window.blit(exit, (x,y))
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
