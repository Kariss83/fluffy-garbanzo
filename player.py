#! usr/bin/env python3
# coding: utf-8

class Player:
    """This class will allow the creation of the playable character
    (aka. Chuck) and allow him to move through the maze"""

    def __init__(self, sprite, lvl):
        #we load the sprite of the playale character with pygame
        self.sprite = 0
        #we need to indicate the lvl in order to get the initial position
        self.level = lvl
        #in a particular lvl we have to look for the coordinates of the entrance
        #should be able to get a tuple with its position in the maze structure
        self.case_x = 0
        self.case_y = 0
        #inventory is empty at creation
        self.inventory = []

    def move_to(self, direction)
        """Method that allow to move the player in any direction"""

        #to the right
        if direction == "right":
            #we must not go over the lvl structure
            if self.case_x < 14:
                #we must not go through a wall
                if self.level.structure[self.case_y][self.case_x + 1] =! "x":
                    self.case_x += 1

        #to the left
        if direction == "left":
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] =! "x":
                    self.case_x -= 1

        #going up
        if direction == "up":
            if self.case_y > 0:
                if self.level.structure[self.case_y -1][self.case_x] =! "x":
                    self.case_y -= 1
        #going down
        if direction == "down":
            if self.case_y > 0:
                if self.level.structure[self.case_y +1][self.case_x] =! "x":
                    self.case_y += 1
        


