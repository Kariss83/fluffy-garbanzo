#! usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame

PIXELS_PER_SPRITE = 60


class Player:
    """This class will allow the creation of the playable character
    (aka. Chuck) and allow him to move through the maze"""

    def __init__(self, sprite, lvl):
        # we load the sprite of the playable character with pygame
        # self.sprite = pygame.image.load(sprite).convert()
        # we need to indicate the lvl in order to get the initial position
        self.lvl = lvl
        self.sprite = pygame.image.load(sprite).convert_alpha()
        # in a particular lvl we have to look for the coordinates of the entrance
        # should be able to get a tuple with its position in the maze structure
        self.case_x = lvl.entry[0]
        self.case_y = lvl.entry[1]
        # inventory is empty at creation
        self.inventory = 0

    @property
    def x(self):
        return self.case_x * PIXELS_PER_SPRITE

    @property
    def y(self):
        return self.case_y * PIXELS_PER_SPRITE

    def move_to(self, direction):
        """Method that allow to move the player in any direction"""

        # to the right
        if direction == "right":
            # We can only move in a position that is not a wall (all stored in lvl.empty)
            if (self.case_y, self.case_x + 1) in self.lvl.empty:
                self.case_x += 1
                # self.x = self.case_x * PIXELS_PER_SPRITE
        # to the left
        if direction == "left":
            if (self.case_y, self.case_x - 1) in self.lvl.empty:
                self.case_x -= 1
                # self.x = self.case_x * PIXELS_PER_SPRITE
        # going up
        if direction == "up":
            if (self.case_y - 1, self.case_x) in self.lvl.empty:
                self.case_y -= 1
                # self.y = self.case_y * PIXELS_PER_SPRITE
        # Going down
        if direction == "down":
            if (self.case_y + 1, self.case_x) in self.lvl.empty:
                self.case_y += 1
                # self.y = self.case_y * PIXELS_PER_SPRITE

    def Pickup(self):
        if (self.case_x, self.case_y) in self.lvl.items:
            self.inventory += 1
            self.lvl.items.remove((self.case_x, self.case_y))


def main():
    maze = Maze('data/maze_structure.csv')
    maze.lvl_creation()
    chuck = Player(0, maze)


if __name__ == "__main__":
    main()
