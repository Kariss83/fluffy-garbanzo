#! usr/bin/env/python3
# coding: utf-8

import os
import time
import random

import pygame

from pygame.locals import *

from player import Player
from maze import Maze
from items import Item
from constants import *

"""And now the program itself"""
# pygame start
pygame.init()
os.environ["SDL_VIDEODRIVER"] = "dummy"

# random initalization
random.seed()

# initiating pygame window at the size of our total sprites + inventory display
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + PIXELS_PER_SPRITE), RESIZABLE)
# game icon
icon = pygame.image.load(ICON_IMAGE)
pygame.display.set_icon(icon)
# title
pygame.display.set_caption(WINDOW_TITLE)

# main loop
is_running = True
while is_running:
    # control loops to navigate between the lobby and the game
    remain_in_lobby = True
    remain_in_game = True

    # Load and display of the game lobby
    lobby = pygame.image.load(LOBBY_IMAGE).convert()
    window.blit(lobby, (0, 0))

    # Refresh the display
    pygame.display.flip()

    while remain_in_lobby:
        # Limitation of loop speed
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # In case the user wants to qui we put all control variable
            # the value 0
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                is_running = False
                remain_in_game = False
                remain_in_lobby = False

            elif event.type == KEYDOWN:
                remain_in_lobby = False  # leaving the lobby

    # now that we exit the lobby we have to create the game structure
    # background loading
    background = pygame.image.load(BACKGROUND_IMAGE).convert()

    # lvl generation
    maze = Maze('data/maze_structure.csv')
    maze.creation()

    # hero generation
    macgyver = Player('data/ressource/MacGyver.png', maze)

    # items generation
    needle = Item(maze, NEEDLE_SPRITE)
    plastic_tube = Item(maze, PLASTIC_TUBE_SPRITE)
    ether = Item(maze, ETHER_SPRITE)
    ether.placing()
    needle.placing()
    plastic_tube.placing()

    # display of the created world
    maze.display(window, WALL_IMAGE, GARDIAN_IMAGE)
    ether.display_item(window)
    needle.display_item(window)
    plastic_tube.display_item(window)

    # Display the inventory counter
    inventory = pygame.image.load(INVENTORY_LIST[0])
    window.blit(inventory, (0, 900))

    # now entering the game loop itself
    while remain_in_game:

        # Loop speed limitation
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # If the user wants to quit we set control loops to 0
            if event.type == QUIT:
                remain_in_game = False
                control_loop = False

            elif event.type == KEYDOWN:
                # If the user only press escape he comes back to the lobby
                if event.key == K_ESCAPE:
                    remain_in_game = False

                # Moving MacGyver using the arrow keys
                elif event.key == K_RIGHT:
                    macgyver.move_to('right')
                elif event.key == K_LEFT:
                    macgyver.move_to('left')
                elif event.key == K_UP:
                    macgyver.move_to('up')
                elif event.key == K_DOWN:
                    macgyver.move_to('down')

            # We try to pick up the item on the position we are after every movement
            macgyver.Pickup()
            # If an object is picked up, he should not be displayed anymore
            ether.stop_display(macgyver)
            needle.stop_display(macgyver)
            plastic_tube.stop_display(macgyver)

        # Display of the new situation after every movements
        window.blit(background, (0, 0))
        maze.display(window, WALL_IMAGE, GARDIAN_IMAGE)
        ether.display_item(window)
        needle.display_item(window)
        plastic_tube.display_item(window)
        window.blit(macgyver.sprite, (macgyver.x, macgyver.y))

        # Display the inventory counter
        inventory = pygame.image.load(INVENTORY_LIST[macgyver.inventory])
        window.blit(inventory, (0, 900))

        # Refresh display
        pygame.display.flip()

        # We check for victory (at the exit with all items in inventory)
        if maze.structure[macgyver.case_x][macgyver.case_y] == 'e':
            if macgyver.inventory == 3:
                # We display the win page
                win = pygame.image.load(WIN).convert()
                window.blit(win, (0, 0))
                pygame.display.flip()
                time.sleep(5.5)
                # And we restart the game
                remain_in_game = False
            # If we goes the guardian without all the items, we loose :
            else:
                # we display the loose page
                loss = pygame.image.load(LOSS).convert()
                window.blit(loss, (0, 0))
                pygame.display.flip()
                time.sleep(5.5)
                # And restart the game
                remain_in_game = False

if __name__ == "__main__":
    main()