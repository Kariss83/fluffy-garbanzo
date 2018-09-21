#! usr/bin/env/python3
# coding: utf-8

from maze import *
from items import *
from player import *
import os
import pygame
from pygame.locals import *

"""Here are all the constants we need in the game"""
#window parameter
SPRITE_NUMBER = 15
PIXELS_PER_SPRITE = 120
WINDOW_SIZE = SPRITE_NUMBER + PIXELS_PER_SPRITE
#window tuning
WINDOW_TITLE = "Escape game MacGyver"
ICON_IMAGE = 'data/ressource/tile-crusader-logo.png'
#game images
LOBBY_IMAGE = "data/ressource/accueil.png"
BACKGROUND_IMAGE = "data/ressource/fond.jpg"
WALL_IMAGE = "data/ressource/mur.png"
GARDIAN_IMAGE = "data/ressource/Gardien.png"
HERO_IMAGE = "data/ressource/MacGyver.png"
ETHER_SPRITE = "data/ressource/ether.png"
NEEDLE_SPRITE = "data/ressource/aiguille.png"
PLASTIC_TUBE_SPRITE =  "data/ressource/tube_plastique.png"

"""And now the program itself"""
#pygame start
pygame.init()
os.environ["SDL_VIDEODRIVER"] = "dummy"


#initiating pygame window at the size of our total sprites
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
#game icon
icon = pygame.image.load(ICON_IMAGE)
pygame.display.set_icon(icon)
#title
pygame.display.set_caption(WINDOW_TITLE)



#Main loop
control = 1
while control:
    #Load and display of the game lobby
    lobby = pygame.image.load(LOBBY_IMAGE).convert()
    window.blit(lobby, (0,0))

	#Refresh
    pygame.display.flip()

	#Variables that have to get the value 1 at each row to get into the game
    remain_in_game = 1
    remain_in_lobby = 1
    
    #Lobby loop
    while remain_in_lobby:
    
        #Limitation of loop speed
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            #In case the user wants to qui we put all control variable 
            #the value 0
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            	control = 0
            	remain_in_game = 0
            	remain_in_lobby = 0
				
            elif event.type == KEYDOWN:				
                remain_in_lobby = 0	#leaving the lobby
                

	#now that we exit the lobby we have to create the game structure			
    #background loading
    background = pygame.image.load(BACKGROUND_IMAGE).convert()

    #Lvl generation 
    maze = Maze('data/maze_structure.csv')
    maze.lvl_creation()
		
	#Hero creation
    macgyver = Player(HERO_IMAGE, maze)
        
    #Item creation
    ether = Item(maze, ETHER_SPRITE)
    needle = Item(maze, NEEDLE_SPRITE)
    plastic_tube = Item(maze, PLASTIC_TUBE_SPRITE)
    ether.placing(maze)
    needle.placing(maze)
    plastic_tube.placing(maze)
        
    #display of the created world
    maze.lvl_display(window, WALL_IMAGE, GARDIAN_IMAGE)
    ether.display_item(window)
    needle.display_item(window)
    plastic_tube.display_item(window)
        
    #BOUCLE DE JEU
    while remain_in_game:
	
	    #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)
        
        for event in pygame.event.get():
            #Si l'utilisateur quitte, on met la variable qui continue le jeu
            #ET la variable générale à 0 pour fermer la fenêtre
            if event.type == QUIT:
                remain_in_game = 0
                control = 0
		
            elif event.type == KEYDOWN:
                #Si l'utilisateur presse Echap ici, on revient seulement au menu
                if event.key == K_ESCAPE:
                    remain_in_game = 0
					
                #Touches de déplacement de Donkey Kong
                elif event.key == K_RIGHT:
                    macgyver.move_to('right', maze)
                elif event.key == K_LEFT:
                    macgyver.move_to('left', maze)
                elif event.key == K_UP:
                    macgyver.move_to('up', maze)
                elif event.key == K_DOWN:
                    macgyver.move_to('down', maze)			
			
        #Affichages aux nouvelles positions
        window.blit(background, (0,0))
        maze.lvl_display(window)
        window.blit(macgyver.sprite, (macgyver.x, macgyver.y)) 
        pygame.display.flip()

        #Victoire -> Retour à l'accueil
        if maze.structure[macgyver.case_y][macgyver.case_x] == 'exit':
            remain_in_game = 0

