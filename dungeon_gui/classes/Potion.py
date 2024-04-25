import pygame

potion_tileset = pygame.image.load("Dungeon_Resolver/dungeon_gui/assets/0x72_16x16DungeonTileset.v5.png")

TILE_SIZE = 16
SCALE_FACTOR = 2

class Potion():
    def __init__(self, potion_value:int, potion_tileset=potion_tileset):
        self.potion_value = potion_value
        self.potion_tileset = potion_tileset
        self.potion_pos_x, self.potion_pos_y = (7, 1)
        self.potion_tile_x, self.potion_tile_y = (12, 11)

    def render_potion(self, screen, room_x, room_y, scale_factor):
        potion_surface = self.potion_tileset.subsurface(pygame.Rect(self.potion_tile_x * TILE_SIZE, self.potion_tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        scaled_potion_surface = pygame.transform.scale(potion_surface, (TILE_SIZE * scale_factor, TILE_SIZE * scale_factor))
        screen.blit(scaled_potion_surface, (self.potion_pos_x * TILE_SIZE * scale_factor + room_x, self.potion_pos_y * TILE_SIZE * scale_factor + room_y))