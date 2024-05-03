"""
This module is part of the dungeon_gui package, for the graphical representation of the dungeon
"""

import pygame

from collectable import Collectable

potion_tileset = pygame.image.load("Dungeon_Resolver/dungeon_gui/assets/0x72_16x16DungeonTileset.v5.png")

TILE_SIZE = 16
SCALE_FACTOR = 2
# TODO Remember to change tile basing to the value
class Potion(Collectable):
    """
    This class describes the representation of the Potion Object 
    """
    def __init__(self, potion_value:int, potion_tileset=potion_tileset):
        super().__init__()
        self.potion_value = potion_value
        self.potion_tileset = potion_tileset
        self.potion_pos_x, self.potion_pos_y = (12.95, 3.1)

        if self.potion_value == 10:
            self.potion_tile_x, self.potion_tile_y = (12, 11)
        elif self.potion_value == 30:
            self.potion_tile_x, self.potion_tile_y = (12, 12)
        else:
            self.potion_tile_x, self.potion_tile_y = (12, 13)


    def render_collectable(self, screen, scale_factor):
        """
        Rendering of the Potion Object on the screen using a tile set

        Parameters
        ----------
        :param screen: Screen where dungeon_gui runs
        :type screen: pygame Surface
        :param scale_factor: Object scale factor 
        :param type: scale_factor: int
        """
        potion_surface = self.potion_tileset.subsurface(pygame.Rect(self.potion_tile_x * TILE_SIZE, self.potion_tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        scaled_potion_surface = pygame.transform.scale(potion_surface, (TILE_SIZE * scale_factor, TILE_SIZE * scale_factor))
        
        if self.collected and self.alpha > 0:
            self.alpha -= 8
            scaled_potion_surface.set_alpha(self.alpha)
        elif self.alpha <= 0:
            return
        
        screen.blit(scaled_potion_surface, (self.potion_pos_x * TILE_SIZE * scale_factor, self.potion_pos_y * TILE_SIZE * scale_factor))