#! usr/bin/env python3
# -*- coding: utf-8 -*-


from maze import *
from items import *

PIXELS_PER_SPRITE = 120


class Player:
    """This class will allow the creation of the playable character
    (aka. Chuck) and allow him to move through the maze"""

    def __init__(self, sprite, lvl):
        #we load the sprite of the playale character with pygame
        #self.sprite = pygame.image.load(sprite).convert()
        #we need to indicate the lvl in order to get the initial position
        self.level = lvl
        #in a particular lvl we have to look for the coordinates of the entrance
        #should be able to get a tuple with its position in the maze structure
        self.case_x = lvl.entry[0][0]
        self.case_y = lvl.entry[0][1]
        self.x = self.case_x * PIXELS_PER_SPRITE
        self.y = self.case_y * PIXELS_PER_SPRITE
        #inventory is empty at creation
        self.inventory = 0

    def move_to(self, direction, lvl):
        """Method that allow to move the player in any direction"""

        #to the right
        if direction == "right":
            if (self.case_y, self.case_x + 1) in lvl.empty:
                print('vous avez le droit')
                lvl.structure[self.case_y][self.case_x] = '0'
                self.case_x += 1
                lvl.structure[self.case_y][self.case_x] = 'macgyver'
            else:
                print('vous n''avez pas le droit')
        
        if direction == "left":
            if (self.case_y, self.case_x - 1) in lvl.empty:
                print('vous avez le droit')
                lvl.structure[self.case_y][self.case_x] = '0'
                self.case_x -= 1
                lvl.structure[self.case_y][self.case_x] = 'macgyver'
            else:
                print('vous n''avez pas le droit')
        
                
        if direction == "up":
            if (self.case_y - 1, self.case_x) in lvl.empty:
                print('vous avez le droit')
                lvl.structure[self.case_y][self.case_x] = '0'
                self.case_y -= 1
                lvl.structure[self.case_y][self.case_x] = 'macgyver'
            else:
                print('vous n''avez pas le droit')
        
        if direction == "down":
            if (self.case_y + 1, self.case_x) in lvl.empty:
                print('vous avez le droit')
                lvl.structure[self.case_y][self.case_x] = '0'
                self.case_y += 1
                lvl.structure[self.case_y][self.case_x] = 'macgyver'
            else:
                print('vous n''avez pas le droit')


    def Pickup(self, lvl):
        if (self.case_x, self.case_y) in lvl.items:
            print('vous etes sur un item, vous le ramassez ! /n')
            self.inventory += 1
            lvl.structure[self.case_x][self.case_y] = '0'
            lvl.items.remove((self.case_x, self.case_y))
            print(lvl.items)
                
                
                
def main():
    maze = Maze('data/maze_structure.csv')
    maze.lvl_creation()
    chuck = Player(0, maze)
    

if __name__ == "__main__":
    main()
