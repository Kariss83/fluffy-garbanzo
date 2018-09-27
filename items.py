#! usr/bin/env python3
# -*- coding: utf-8 -*-

import random

import pygame

PIXELS_PER_SPRITE = 60


class Item:
    """This class will allow the creation of any item that lies on the game
    structure (object or NPC)"""

    def __init__(self, lvl, sprite):
        # default coordinate
        self.case_x = 0
        self.case_y = 0
        # Item sprite is loaded here
        self.sprite = pygame.image.load(sprite).convert()
        self.lvl = lvl
        # used to know if the item as been picked up, 0 is for picked up items
        self.state = 1

    @property
    def x(self):
        """We need to have the x position in pixel in order to display using pygame"""
        return self.case_x * PIXELS_PER_SPRITE

    @property
    def y(self):
        """we need to have the y position in pixel in order to display using pygame"""
        return self.case_y * PIXELS_PER_SPRITE

    def placing(self):
        """We randomly place the item in an empty case """
        # generating a random index to get a position in maze.empty_for_obj
        k = random.randint(0, len(self.lvl.empty_for_obj) - 1)
        # getting the coordinate in maze.empty_for_obj[k]
        self.case_x = self.lvl.empty_for_obj[k][1]
        self.case_y = self.lvl.empty_for_obj[k][0]
        # self.case_x, self.case_y = random.choice(self.lvl.empty_for_obj)
        self.lvl.items.append((self.case_x, self.case_y))
        del (self.lvl.empty_for_obj[k])
        # self.lvl.empty_for_obj.remove((self.case_x, self.case_y))

    def display_item(self, window):
        """We first check if the item is picked up and then we display its sprite ate the right location"""
        if self.state:
            window.blit(self.sprite, (self.x, self.y))

    def stop_display(self, player):
        """If the player goes into an item position, it should not be displayed anymore"""
        if (player.case_x, player.case_y) == (self.case_x, self.case_y):
            self.state = 0


def main():
    pass


if __name__ == "__main__":
    main()
