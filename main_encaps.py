#! usr/bin/env/python3
# -*- coding: utf-8 -*-
""" This file is the main file of the game, the one you should execute in
order to run it.
"""
import os
import random

import pygame

from pygame.locals import *

from player import Player
from maze import Maze
from items import Item
from constants import *


class Game:
    """This is the main class, the one containing the maze, the character and
    the items, used to display the whole environment
    """

    def __init__(self):
        """"We need to initialize here all that we need for the game to run :
        character, item, maze and other display utilities
        """
        self.is_running = False

        # pygame start
        pygame.init()
        os.environ["SDL_VIDEODRIVER"] = "dummy"

        # random initialization
        random.seed()

        # initiating pygame window at the size of our total sprites
        # + inventory display
        self.window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE +
                                               PIXELS_PER_SPRITE), RESIZABLE)
        # game icon
        icon = pygame.image.load(ICON_IMAGE)
        pygame.display.set_icon(icon)
        # title
        pygame.display.set_caption(WINDOW_TITLE)

        # init of all other variables
        self.background = None
        self.inventory = None
        self.maze = None
        self.macgyver = None
        self.needle = None
        self.plastic_tube = None
        self.ether = None

        self.remain_in_game = True
        self.remain_in_lobby = True

    def lobby(self):
        """" We start the lobby of a given game with a lobby screen that
        will vanish to let the player start the actual game once he has
        pressed any key or let him leave if he press exit twice
        """
        # Limitation of loop speed
        pygame.time.Clock().tick(30)

        # display of the lobby
        lobby = pygame.image.load(LOBBY_IMAGE).convert()
        self.window.blit(lobby, (0, 0))
        pygame.display.flip()

        # We need to get to remain_in_game the value True so that if it's not
        # the first game the user will still be able to enter the game itself
        self.remain_in_game = True

        for event in pygame.event.get():
            # In case the user wants to qui we put all control variable
            # the value 0
            if event.type == QUIT or (event.type == KEYDOWN and
                                      event.key == K_ESCAPE):
                self.is_running = False
                self.remain_in_game = False
                self.remain_in_lobby = False

            elif event.type == KEYDOWN:
                self.remain_in_lobby = False  # leaving the lobby

    def visual_representation(self):
        """" This method allow us to display the main screen of the game at
        the beginning with the maze, its structure,the items at their original
        position, the guardian and the player
        """
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
        self.inventory = pygame.image.load(INVENTORY_LIST[0])
        self.window.blit(self.inventory, (0, 900))

    def move(self):
        """ This method allow us to make the player move and pick up items
        on the destination case updating all the positions
        """
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
                    self.remain_in_lobby = True

                # Moving MacGyver using the arrow keys
                elif event.key == K_RIGHT:
                    self.macgyver.move_to('right')
                elif event.key == K_LEFT:
                    self.macgyver.move_to('left')
                elif event.key == K_UP:
                    self.macgyver.move_to('up')
                elif event.key == K_DOWN:
                    self.macgyver.move_to('down')

            # We try to pick up the item on the position we are after every
            # movement
            self.macgyver.Pickup()
            # If an object is picked up, he should not be displayed anymore
            self.ether.stop_display(self.macgyver)
            self.needle.stop_display(self.macgyver)
            self.plastic_tube.stop_display(self.macgyver)

    def reload_graphic(self):
        """ This method allow us to recharge the graphic environment after
        each movement
        """
        # Display of the new situation after every movements
        self.window.blit(self.background, (0, 0))
        self.maze.display(self.window, WALL_IMAGE, GARDIAN_IMAGE)
        self.ether.display_item(self.window)
        self.needle.display_item(self.window)
        self.plastic_tube.display_item(self.window)
        self.window.blit(self.macgyver.sprite, (self.macgyver.x,
                                                self.macgyver.y))

        # Display the inventory counter
        self.inventory = pygame.image.load(
            INVENTORY_LIST[self.macgyver.inventory])
        self.window.blit(self.inventory, (0, 900))

        # Refresh display
        pygame.display.flip()

    def display_endgame(self):
        """ This method only intervene when it is the end game and will
        display either the win screen or the loss screen then wait for the
        user to press a key to bring him back to the lobby
        """
        # We check for victory (at the exit with all items in inventory)
        if self.macgyver.inventory == NUMBER_OF_ITEMS:
            # We display the win page
            win = pygame.image.load(WIN).convert()
            self.window.blit(win, (0, 0))
            pygame.display.flip()
            end_key_pressed = False
            while not end_key_pressed:
                # Limitation of loop speed
                pygame.time.Clock().tick(30)
                for event in pygame.event.get():
                    # If the user wants to restart he just has to press
                    # another key
                    if event.type == KEYDOWN:
                        self.remain_in_game = False
                        self.remain_in_lobby = True
                        end_key_pressed = True
        # If we goes the guardian without all the items, we loose :
        else:
            # we display the loose page
            loss = pygame.image.load(LOSS).convert()
            self.window.blit(loss, (0, 0))
            pygame.display.flip()
            # Limitation of loop speed
            end_key_pressed = False
            while not end_key_pressed:
                pygame.time.Clock().tick(30)

                for event in pygame.event.get():
                    # If the user wants to restart he just has to press
                    # another key
                    if event.type == KEYDOWN:
                        self.remain_in_game = False
                        self.remain_in_lobby = True
                        end_key_pressed = True

    def run(self):
        """" This method represents the game itself : you first arrive at
        lobby, if you press a key you are in game and moving, with you reach
        the guardian, we check for victory and display the appropriate
        """
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
