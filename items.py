#! usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from typing import List, Any

import pygame

PIXELS_PER_SPRITE = 60


class Item:
    """This class will allow the creation of any item that lies on the game
    structure (object or NPC)"""

    def __init__(self, lvl, sprite):
        self.case_x = 0
        self.case_y = 0
        self.sprite = pygame.image.load(sprite).convert()
        self.level = lvl
        self.state = 1

    @property
    def x(self):
        return self.case_y * PIXELS_PER_SPRITE

    @property
    def y(self):
        return self.case_x * PIXELS_PER_SPRITE

    def placing(self, lvl):
        # -tc- on n'exécute seed() que une fois par programme
        random.seed()
        # k = random.randint(0, len(lvl.empty_for_obj) - 1)
        # self.case_x = lvl.empty_for_obj[k][1]
        # self.case_y = lvl.empty_for_obj[k][0]
        # lvl.items.append((self.case_x, self.case_y))
        # del (lvl.empty_for_obj[k])
        self.case_x,  self.case_y = random.choice(self.level.empty_for_obj)
        self.level.items.append((self.case_x,  self.case_y))
        self.level.empty_for_obj.remove((self.case_x,  self.case_y))

    def display_item(self, window):
        if self.state:
            # -tc- Attention d'afficher les sprites dans le bon ordre
            window.blit(self.sprite, (self.x, self.y))

    def stop_display(self, player):
        if (player.case_x, player.case_y) == (self.case_x, self.case_y):
            self.state = 0

def main():
    pass


if __name__ == "__main__":
    main()
