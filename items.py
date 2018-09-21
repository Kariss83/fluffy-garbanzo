#! usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import pygame


PIXELS_PER_SPRITE = 120

class Item:
    """This class will allow the creation of any item that lies on the game
    structure (object or NPC)"""
    
    def __init__(self, lvl, sprite, name):
        self.case_x = 0
        self.case_y = 0
        #self.sprite = pygame.image.load(sprite).convert()
        self.level = lvl
        self.name = name

    def placing(self, lvl):

        random.seed()
        k = random.randint(0, len(lvl.empty_for_obj) -1)
        self.case_x = lvl.empty_for_obj[k][0]
        self.case_y = lvl.empty_for_obj[k][1]
        lvl.items.append((self.case_x, self.case_y))
        del(lvl.empty_for_obj[k])
        lvl.structure[self.case_x][self.case_y] = self.name
    
        
        
    def display_item(self, window):
       #x = self.case_x * PIXELS_PER_SPRITE
       #y = self.case_y * PIXELS_PER_SPRITE
       #window.blit(self.sprite, (x,y))
       pass


def main() :
    pass
	
	
if __name__ == "__main__":
    main()





