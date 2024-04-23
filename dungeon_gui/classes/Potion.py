import pygame

potion_tileset = pygame.image.load("dungeon_resolver/dungeon_gui/assets/dungeon_tileset.png")


class Potion():
    def __init_(self, potion_value=0, potion_tileset=potion_tileset, potion_pos_x=potion_pos_x, potion_pos_y=potion_pos_y):
        self.potion_value = potion_value
        self.potion_tileset = potion_tileset
        self.potion_pos_x, self.potion_pos_y = (1, 7)
        self.loot_tile_x, self.loot_tile_y = (10, 8)
