import pygame

key_tileset = pygame.image.load("dungeon_resolver/dungeon_gui/assets/dungeon_tileset.png")

TILE_SIZE = 16

class Key():
    def __init__(self, key_tileset=key_tileset):
        self.key_tileset = key_tileset
        self.key_pos_x, self.key_pos_y = (8, 5)
        self.key_tile_x, self.key_tile_y = (9, 9)

    def render_key(self, screen, room_x, room_y, scale_factor):
        key_surface = key_tileset.subsurface(pygame.Rect(self.key_tile_x * TILE_SIZE, self.key_tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        scaled_key_surface = pygame.transform.scale(key_surface, (TILE_SIZE * scale_factor, TILE_SIZE * scale_factor))
        screen.blit(scaled_key_surface, (self.key_pos_x * TILE_SIZE * scale_factor + room_x, self.key_pos_y * TILE_SIZE * scale_factor + room_y))