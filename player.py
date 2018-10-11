#! usr/bin/env python3
# -*- coding: utf-8 -*-
"""This file contains the player module, in which we define the player class
used to created macgyver the hero of the game.
"""
import pygame

PIXELS_PER_SPRITE = 60


class Player(object):
    """This class will allow the creation of the playable character
    (aka. Chuck) and allow him to move through the maze
    """

    def __init__(self, sprite, lvl):
        # we load the sprite of the playable character with pygame
        # self.sprite = pygame.image.load(sprite).convert()
        # we need to indicate the lvl in order to get the initial position
        self.lvl = lvl
        self.sprite = pygame.image.load(sprite).convert_alpha()
        # in a particular lvl we have to look for the coordinates of the
        # entrance should be able to get a tuple with its position in the
        # maze structure
        self.case_x = lvl.entry[0]
        self.case_y = lvl.entry[1]
        # inventory is empty at creation
        self.inventory = 0

    @property
    def x_pix(self):
        """This property is useful for position in pixel in pygame
        """
        return self.case_x * PIXELS_PER_SPRITE

    @property
    def y_pix(self):
        """This property is useful for position in pixel in pygame
        """
        return self.case_y * PIXELS_PER_SPRITE

    def move_to(self, direction):
        """Method that allow to move the player in any direction
        """

        # to the right
        if direction == "right":
            # We can only move in a position that is not a wall
            # (all stored in lvl.empty)
            if (self.case_y, self.case_x + 1) in self.lvl.empty:
                self.case_x += 1
        # to the left
        if direction == "left":
            if (self.case_y, self.case_x - 1) in self.lvl.empty:
                self.case_x -= 1
        # going up
        if direction == "up":
            if (self.case_y - 1, self.case_x) in self.lvl.empty:
                self.case_y -= 1
        # Going down
        if direction == "down":
            if (self.case_y + 1, self.case_x) in self.lvl.empty:
                self.case_y += 1

    def pickup(self):
        """ This method allow the character to try to pick up an item
        if there is one on his postion
        """
        if (self.case_x, self.case_y) in self.lvl.items:
            self.inventory += 1
            self.lvl.items.remove((self.case_x, self.case_y))



if __name__ == "__main__":
    """ This is a test function
    """
    maze = Maze('data/maze_structure.csv')
    maze.lvl_creation()
    chuck = Player(0, maze)        
