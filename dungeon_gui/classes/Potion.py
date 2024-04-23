import pygame

potion_tileset = pygame.image.load("dungeon_resolver/dungeon_gui/assets/dungeon_tileset.png")


class Potion():
    def __init__(self, potion_value=0, potion_tileset=potion_tileset):
        self.potion_value = potion_value
        self.potion_tileset = potion_tileset
        self.potion_pos_x, self.potion_pos_y = (7, 1)
        self.potion_tile_x, self.potion_tile_y = (9, 8)
