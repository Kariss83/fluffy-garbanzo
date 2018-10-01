#! usr/bin/env/python3
# -*- coding: utf-8 -*-

import os
import random

import pygame

from constants import *
from pygame.locals import *


class Lobby:

    def __init__(self):
        pass

    def start_lobby(self):
        # pygame start
        pygame.init()
        os.environ["SDL_VIDEODRIVER"] = "dummy"

        # random initalization
        random.seed()

    def generate_window(self):
        # initiating pygame window at the size of our total sprites + inventory display
        window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + PIXELS_PER_SPRITE), RESIZABLE)
        # game icon
        icon = pygame.image.load(ICON_IMAGE)
        pygame.display.set_icon(icon)
        # title
        pygame.display.set_caption(WINDOW_TITLE)




if __name__ == "__main__":
    lobby = Lobby()
    lobby.start_lobby()
    lobby.generate_window()
    pygame.display.flip()