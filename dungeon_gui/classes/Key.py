import pygame

potion_tileset = pygame.image.load("dungeon_resolver/dungeon_gui/assets/dungeon_tileset.png")

TILE_SIZE = 16

class Key():
    def __init__(self, key_tileset=potion_tileset):
        self.key_tileset = key_tileset
        self.key_pos_x, self.key_pos_y = (7, 5)
        self.key_tile_x, self.key_tile_y = (9, 9)

    def render_key(self, screen):
        screen.blit(self.key_tileset, (self.key_pos_x * TILE_SIZE, self.key_pos_y * TILE_SIZE), (self.key_tile_x * TILE_SIZE, self.key_tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))