#! usr/bin/env python3
# coding: utf-8

import random


class Item:
    """This class will allow the creation of any item that lies on the game
    structure (object or NPC)"""
    
    def __init__(self, lvl, sprite):
        self.case_x = 0
        self.case_y = 0
        self.sprite = sprite
        self.level = lvl

    def placing_items(self):
        x = 0
        y = 0
        while self.level.structure[y][x] != 'o':
            x = random.randint(14)
            y = random.randint(14)
        self.case_x = x
        self.case_y = y


