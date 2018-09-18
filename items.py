#! usr/bin/env python3
# -*- coding: utf-8 -*-

import random


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


def main() :
    pass
	
	
if __name__ == "__main__":
    main()





