#! usr/bin/env/python3
# -*- coding: utf-8 -*-

import os
import time
import random

import pygame

from pygame.locals import *

from player import Player
from maze import Maze
from items import Item
from constants import *


class Game:

    def __init__(self):
        self.is_running = False

        # pygame start
        pygame.init()
        os.environ["SDL_VIDEODRIVER"] = "dummy"

        # random initalization
        random.seed()

        # initiating pygame window at the size of our total sprites + inventory display
        self.window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + PIXELS_PER_SPRITE), RESIZABLE)
        # game icon
        icon = pygame.image.load(ICON_IMAGE)
        pygame.display.set_icon(icon)
        # title
        pygame.display.set_caption(WINDOW_TITLE)

        # init of all other variables
        self.background = None
        self.maze = None
        self.macgyver = None
        self.needle = None
        self.plastic_tube = None
        self.ether = None

        self.remain_in_game = True
        self.remain_in_lobby = True

    def lobby(self):
        # Limitation of loop speed
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # In case the user wants to qui we put all control variable
            # the value 0
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.is_running = False
                self.remain_in_game = False
                self.remain_in_lobby = False

            elif event.type == KEYDOWN:
                self.remain_in_lobby = False  # leaving the lobby

    def visual_representation(self):
        # now that we exit the lobby we have to create the game structure
        # background loading
        self.background = pygame.image.load(BACKGROUND_IMAGE).convert()

        # lvl generation
        self.maze = Maze('data/maze_structure.csv')
        self.maze.creation()

        # hero generation
        self.macgyver = Player('data/resource/MacGyver.png', self.maze)

        # items generation
        self.needle = Item(self.maze, NEEDLE_SPRITE)
        self.plastic_tube = Item(self.maze, PLASTIC_TUBE_SPRITE)
        self.ether = Item(self.maze, ETHER_SPRITE)
        self.ether.placing()
        self.needle.placing()
        self.plastic_tube.placing()

        # display of the created world
        self.maze.display(self.window, WALL_IMAGE, GARDIAN_IMAGE)
        self.ether.display_item(self.window)
        self.needle.display_item(self.window)
        self.plastic_tube.display_item(self.window)

        # Display the inventory counter
        inventory = pygame.image.load(INVENTORY_LIST[0])
        self.window.blit(inventory, (0, 900))

    def move(self):
        # Loop speed limitation
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # If the user wants to quit we set control loops to 0
            if event.type == QUIT:
                self.remain_in_game = False
                self.is_running = False

            elif event.type == KEYDOWN:
                # If the user only press escape he comes back to the lobby
                if event.key == K_ESCAPE:
                    self.remain_in_game = False

                # Moving MacGyver using the arrow keys
                elif event.key == K_RIGHT:
                    self.macgyver.move_to('right')
                elif event.key == K_LEFT:
                    self.macgyver.move_to('left')
                elif event.key == K_UP:
                    self.macgyver.move_to('up')
                elif event.key == K_DOWN:
                    self.macgyver.move_to('down')

            # We try to pick up the item on the position we are after every movement
            self.macgyver.Pickup()
            # If an object is picked up, he should not be displayed anymore
            self.ether.stop_display(self.macgyver)
            self.needle.stop_display(self.macgyver)
            self.plastic_tube.stop_display(self.macgyver)

    def reload_graphic(self):
        # Display of the new situation after every movements
        self.window.blit(self.background, (0, 0))
        self.maze.display(self.window, WALL_IMAGE, GARDIAN_IMAGE)
        self.ether.display_item(self.window)
        self.needle.display_item(self.window)
        self.plastic_tube.display_item(self.window)
        self.window.blit(self.macgyver.sprite, (self.macgyver.x, self.macgyver.y))

        # Display the inventory counter
        inventory = pygame.image.load(INVENTORY_LIST[self.macgyver.inventory])
        self.window.blit(inventory, (0, 900))

        # Refresh display
        pygame.display.flip()

    def display_endgame(self):
        # We check for victory (at the exit with all items in inventory)
        if self.macgyver.inventory == NUMBER_OF_ITEMS:
            # We display the win page
            win = pygame.image.load(WIN).convert()
            self.window.blit(win, (0, 0))
            pygame.display.flip()
            time.sleep(5.5)
            # And we restart the game
            self.remain_in_game = False
        # If we goes the guardian without all the items, we loose :
        else:
            # we display the loose page
            loss = pygame.image.load(LOSS).convert()
            self.window.blit(loss, (0, 0))
            pygame.display.flip()
            time.sleep(5.5)
            # And restart the game
            self.remain_in_game = False

    def run(self):
        self.is_running = True
        while self.is_running:
            while self.remain_in_lobby:
                self.lobby()
            self.visual_representation()
            # now entering the game loop itself
            while self.remain_in_game:
                self.move()
                self.reload_graphic()
                if self.maze.is_endgame(self.macgyver):
                    self.display_endgame()


if __name__ == "__main__":
    game = Game()
    game.run()
