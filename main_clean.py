#! usr/bin/env/python3
# coding: utf-8

from maze import *
from items import *
from player import *
import os
import pygame
from pygame.locals import *


control_loop = 1
while control_loop:
    #boucles de contrôle pour savoir où le joueur en est
    remain_in_lobby = 1
    remain_in_game = 1
    
    #message d'accueil
    print("Bienvenue dans l'escape game MacGyver")
    
    while remain_in_lobby:
        decision = input("Si vous désirez quitter tapez 'quit' si vous désirez jouer taper 'play'.")
        if decision == 'quit':
            remain_in_lobby = 0
            remain_in_game = 0
            control_loop = 0
        elif decision == 'play':
            remain_in_lobby = 0
        else:
            print('veuillez taper une commande autorisee')
        
        
    #on entre dans le jeu une fois sortis du lobby
    #on génère alors le lvl
    maze = Maze('data/maze_structure.csv')
    maze.lvl_creation()
    print(maze.empty)
    print(maze.empty_for_obj)
    
    #on génère un hero
    macgyver = Player('data/ressource/MacGyver.png', maze)
    
    #on génère les items
    needle = Item(maze, 'data/ressource/aiguille.png', 'needle')
    plastic_tube = Item(maze, 'data/ressource/tube_plastique.png', 'plastic_tube')
    ether = Item(maze, 'data/ressource/ether.png', 'ether')
    ether.placing(maze)
    print(maze.items)
    needle.placing(maze)
    print(maze.items)
    plastic_tube.placing(maze)
    print(maze.items)
    print(maze.empty)
    print(maze.empty_for_obj)
    
    #on affiche le labytinthe en l'état:
    #for line in maze.structure:
        #print(line)
    print(type(maze.structure))
    for ligne in maze.structure:
        print(ligne)
    
    #on rentre dans le jeu en lui même
    while remain_in_game:
        decision_2 = input("Dans quelle dir voulez vous aller? Si droite tapez dr, si gauche tapez ga, si haut tapez ha, si bas tapez ba : ")
        if decision_2 == 'dr':
            macgyver.move_to('right', maze)
        elif decision_2 == 'ga':
            macgyver.move_to('left', maze)
        elif decision_2 == 'ha':
            macgyver.move_to('up', maze)
        elif decision_2 == 'ba':
            macgyver.move_to('down', maze)
        else:
            print("Veuillez entrer une commande qui vous a été spécifiée")
            
        #On ramasse si besoin
        macgyver.Pickup(maze)
        print('vous avez : ', macgyver.inventory, 'item in your bag /n')
        #on vérifie que l'on ne soit pas arrivé à la fin de labyrinthe
        if (macgyver.case_y, macgyver.case_x) in maze.exit:
        #& macgyver.inventory != str(3):
            if macgyver.inventory != 3:
                print('You lost the game cause you did not pick up all the items /n')
                remain_in_game = 0
            else:
                print('Felicitations vous etes sortis du labyrinthe /n')
                remain_in_game = 0
        
        
        #Si on n'a pas fini le jeu on réaffiche l'état du labyrinthe
        for ligne in maze.structure:
            print(ligne)
    