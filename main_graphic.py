#! usr/bin/env/python3
# coding: utf-8

import os
import time

from pygame.locals import *

# -tc- Eviter les from module import *
from player import *

# -tc- Définir de préférences les constantes globales de l'application dans
# -tc- un fichier séparé, constants.py par exemple

# -tc- On utilise le dièse pour les commentaires. Les guillemets définissent ici une
# -tc- docstring au niveau du module
"""Here are all the constants we need in the game"""
# window parameter
SPRITE_NUMBER = 15
PIXELS_PER_SPRITE = 60
WINDOW_SIZE = SPRITE_NUMBER * PIXELS_PER_SPRITE
# window tuning
WINDOW_TITLE = "Escape game MacGyver"
# -tc- resource ne prend qu'un seul s en anglais
ICON_IMAGE = 'data/ressource/tile-crusader-logo.png'
# game images
LOBBY_IMAGE = "data/ressource/accueil.png"
BACKGROUND_IMAGE = "data/ressource/fond.jpg"
WALL_IMAGE = "data/ressource/mur.png"
GARDIAN_IMAGE = "data/ressource/Gardien.png"
HERO_IMAGE = "data/ressource/MacGyver.png"
ETHER_SPRITE = "data/ressource/ether.png"
NEEDLE_SPRITE = "data/ressource/aiguille.png"
PLASTIC_TUBE_SPRITE = "data/ressource/tube_plastique.png"
INVENTORY_LIST = ["data/ressource/inv0.png",
                  "data/ressource/inv1.png",
                  "data/ressource/inv2.png",
                  "data/ressource/inv3.png"]
WIN = "data/ressource/win.png"
LOSS = "data/ressource/loss.png"

# -tc- mettre le code de lancement de l'application, de préférence dans
# -tc- une classe Main/App/Application/Game ou au minimum dans un fonction
# -tc- main(). Limiter la quantité de code dans le contexte global au minimum

# -tc- Par exemple
class Game:
    """Main class of the application."""

    def __init__(self):
        """Application-level initialization code"""
        pygame.init()
        # -tc- etc.

    def start(self):
        """Main entry point of the application"""
        pass


"""And now the program itself"""
# pygame start
pygame.init()
os.environ["SDL_VIDEODRIVER"] = "dummy"

# initiating pygame window at the size of our total sprites
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + PIXELS_PER_SPRITE), RESIZABLE)
# game icon
icon = pygame.image.load(ICON_IMAGE)
pygame.display.set_icon(icon)
# title
pygame.display.set_caption(WINDOW_TITLE)

# main loop
# -tc- Afin de clarifier leur rôle, utiliser des boléens pour les sentinelles
# -tc- de boucle. Des noms de variables plus descriptifs sont également une
# -tc- aide, comme par exemple is_running = True
control_loop = 1

# -tc- L'utilisation des boucles imbriquées rent le code difficile à lire
# -tc- L'usage de fonctions peut aider
while control_loop:
    # boucles de contrôle pour savoir où le joueur en est
    # -tc- Comme plus haut, utiliser de préférence des valeurs booléennes
    # -tc- pour les sentinelles de boucle.
    remain_in_lobby = 1
    remain_in_game = 1

    # Load and display of the game lobby
    lobby = pygame.image.load(LOBBY_IMAGE).convert()
    window.blit(lobby, (0, 0))

    # Refresh
    pygame.display.flip()

    while remain_in_lobby:
        # Limitation of loop speed
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # In case the user wants to qui we put all control variable
            # the value 0
            # -tc- Utiliser des parenthèses pour clarifier
            # -tc- if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)
            # -tc- beaucoup de gens ignorent que or a une précédence plus faible que and
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                # -tc- utiliser False plutôt que 0
                control_loop = 0
                remain_in_game = 0
                remain_in_lobby = 0

            elif event.type == KEYDOWN:
                # -tc- False
                remain_in_lobby = 0  # leaving the lobby

    # now that we exit the lobby we have to create the game structure
    # background loading
    background = pygame.image.load(BACKGROUND_IMAGE).convert()

    # lvl generation
    # -tc- Maze n'est pas importé, mais présent grâce à from player import *
    maze = Maze('data/maze_structure.csv')
    maze.creation()

    # hero generation
    # -tc- Pourquoi pas de constante pour PLAYER_SPRITE comme les autres ?
    macgyver = Player('data/ressource/MacGyver.png', maze)

    # items generation
    needle = Item(maze, NEEDLE_SPRITE)
    plastic_tube = Item(maze, PLASTIC_TUBE_SPRITE)
    ether = Item(maze, ETHER_SPRITE)
    ether.placing(maze)
    needle.placing(maze)
    plastic_tube.placing(maze)

    # display of the created world
    maze.display(window, WALL_IMAGE, GARDIAN_IMAGE)
    ether.display_item(window)
    needle.display_item(window)
    plastic_tube.display_item(window)

    # Display the inventory counter
    # -tc- Il est possible d'écrire avec Pygame: pygame.font.Font() our pygame.font.SysFont()
    # -tc- pygame.font.Font() te permet d'utiliser un fichier .ttf pour fournir la police.
    inventory = pygame.image.load(INVENTORY_LIST[0])
    window.blit(inventory, (0, 900))

    # on rentre dans le jeu en lui même
    while remain_in_game:

        # moving the hero
        # Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # Si l'utilisateur quitte, on met la variable qui continue le jeu
            # ET la variable générale à 0 pour fermer la fenêtre
            if event.type == QUIT:
                # -tc- Utiliser FALSE
                remain_in_game = 0
                control = 0

            elif event.type == KEYDOWN:
                # Si l'utilisateur presse Echap ici, on revient seulement au menu
                if event.key == K_ESCAPE:
                    # -tc- Utiliser FALSE
                    remain_in_game = 0

                # Touches de déplacement de Donkey Kong
                elif event.key == K_RIGHT:
                    macgyver.move_to('right', maze)
                elif event.key == K_LEFT:
                    macgyver.move_to('left', maze)
                elif event.key == K_UP:
                    macgyver.move_to('up', maze)
                elif event.key == K_DOWN:
                    macgyver.move_to('down', maze)

            # -tc- Le bloc si dessous pourrait de s'exécuter que si il y a eu KEYDOWN + Mouvement
            # On ramasse si besoin
            macgyver.Pickup(maze)
            print('vous avez : ', macgyver.inventory, 'item in your bag /n')
            ether.stop_display(macgyver)
            needle.stop_display(macgyver)
            plastic_tube.stop_display(macgyver)

        # Affichages aux nouvelles positions
        window.blit(background, (0, 0))
        maze.display(window, WALL_IMAGE, GARDIAN_IMAGE)
        ether.display_item(window)
        needle.display_item(window)
        plastic_tube.display_item(window)
        window.blit(macgyver.sprite, (macgyver.x, macgyver.y))

        # Display the inventory counter
        inventory = pygame.image.load(INVENTORY_LIST[macgyver.inventory])
        window.blit(inventory, (0, 900))

        pygame.display.flip()

        # -tc- Chez moi, toute la logique de fin ne s'affiche pas
        # Victoire -> Retour à l'accueil
        # -tc- Pluôt utiliser une méthode comme maze.is_end() que d'accéder directement à la structure
        # -tc- interne de l'objet.
        if maze.structure[macgyver.case_x][macgyver.case_y] == 'e':
            if macgyver.inventory == 3:
                win = pygame.image.load(WIN).convert()
                window.blit(win, (0, 0))
                pygame.display.flip()
                time.sleep(5.5)
                remain_in_game = 0

            else:
                loss = pygame.image.load(LOSS).convert()
                window.blit(loss, (0, 0))
                pygame.display.flip()
                time.sleep(5.5)
                remain_in_game = 0
