"""
This module is part of the dungeon_gui package, for the graphical representation of the dungeon.
Collects some useful constants for other modules.
"""

import pygame

# Custom events
PLAYER_GET_DAMAGE = pygame.USEREVENT + 1
PLAYER_GET_HEAL = pygame.USEREVENT + 2

PLAYER_ENTER_STARTING_POS = (9.4, 16)
PLAYER_ENTER_ENDING_POS = (9.4, 8)

PLAYER_EXIT_ENDING_POS = (9.4, -2)

WEAPON_ENTER_STARTING_POS = (13.5, 18.5)
WEAPON_ENTER_ENDING_POS = (13.5, 10.5)

WEAPON_EXIT_ENDING_POS = (13.5, -3)