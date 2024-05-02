import pygame

from dungeon_gui.classes.collectable import Collectable

key_tileset = pygame.image.load("dungeon_resolver/dungeon_gui/assets/dungeon_tileset.png")

TILE_SIZE = 16

class Key(Collectable):
    def __init__(self, key_tileset=key_tileset):
        super().__init__()
        self.key_tileset = key_tileset
        self.key_pos_x, self.key_pos_y = (12.95, 8.1)
        self.key_tile_x, self.key_tile_y = (9, 9)

    def render_collectable(self, screen, scale_factor):
        key_surface = key_tileset.subsurface(pygame.Rect(self.key_tile_x * TILE_SIZE, self.key_tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        scaled_key_surface = pygame.transform.scale(key_surface, (TILE_SIZE * scale_factor, TILE_SIZE * scale_factor))
        
        if self.collected and self.alpha > 0:
            self.alpha -= 8
            scaled_key_surface.set_alpha(self.alpha)
        elif self.alpha <= 0:
            return

        screen.blit(scaled_key_surface, (self.key_pos_x * TILE_SIZE * scale_factor, self.key_pos_y * TILE_SIZE * scale_factor))