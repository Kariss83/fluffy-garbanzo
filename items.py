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
	
    # -tc- Pourquoi prendre lvl en paramètre alors que c'est un attribut de la classe?
    def placing_items(self, lvl):

	#-tc- seed() a en principe besoin d'être exécuté une fois par programme. Il n'a toutefois en général pas besoin d'être explicite
        random.seed()
        k = random.randint(0, len(lvl.empty) -1)
	# -tc- ou simplement self.case_x, self.case_y = random.choise(self.level.empty)
        self.case_x = lvl.empty[k][0]
        self.case_y = lvl.empty[k][1]
	# -tc- ou simplement self.level.empty.remove((self.case_x, self.case_y))
        del(lvl.empty[k])


def main() :
    pass
	
	
if __name__ == "__main__":
    main()





