import pygame

potion_tileset = pygame.image.load("dungeon_resolver/dungeon_gui/assets/dungeon_tileset.png")

TILE_SIZE = 16

class Potion():
    def __init__(self, potion_value:int, potion_tileset=potion_tileset):
        self.potion_value = potion_value
        self.potion_tileset = potion_tileset
        self.potion_pos_x, self.potion_pos_y = (7, 1)
        self.potion_tile_x, self.potion_tile_y = (9, 8)

    def render_potion(self, screen):
        screen.blit(self.potion_tileset, (self.potion_pos_x * TILE_SIZE, self.potion_pos_y * TILE_SIZE), (self.potion_tile_x * TILE_SIZE, self.potion_tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))