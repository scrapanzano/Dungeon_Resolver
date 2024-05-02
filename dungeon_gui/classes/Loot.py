import pygame

from dungeon_gui.classes.collectable import Collectable

loot_tileset = pygame.image.load("dungeon_resolver/dungeon_gui/assets/dungeon_tileset.png")

TILE_SIZE = 16

class Loot(Collectable):
    def __init__(self, loot_value:int, loot_tileset=loot_tileset):
        super().__init__()
        self.loot_value = loot_value
        self.loot_tileset = loot_tileset
        self.loot_pos_x, self.loot_pos_y = (5.96, 3.2)

        if self.loot_value == 10:
            self.loot_tile_x, self.loot_tile_y = (5, 8)
        elif self.loot_value == 20:
            self.loot_tile_x, self.loot_tile_y = (1, 8)
        elif self.loot_value == 30:
            self.loot_tile_x, self.loot_tile_y = (2, 8)
        else:
            self.loot_tile_x, self.loot_tile_y = (4, 8)

    def render_collectable(self, screen, scale_factor):
        loot_surface = self.loot_tileset.subsurface(pygame.Rect(self.loot_tile_x * TILE_SIZE, self.loot_tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        scaled_loot_surface = pygame.transform.scale(loot_surface, (TILE_SIZE * scale_factor, TILE_SIZE * scale_factor))
        
        if self.collected and self.alpha > 0:
            self.alpha -= 8
            scaled_loot_surface.set_alpha(self.alpha)
        elif self.alpha <= 0:
            return
        
        screen.blit(scaled_loot_surface, (self.loot_pos_x * TILE_SIZE * scale_factor, self.loot_pos_y * TILE_SIZE * scale_factor))