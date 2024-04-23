import pygame

loot_tileset = pygame.image.load("dungeon_resolver/dungeon_gui/assets/dungeon_tileset.png")

loot_pos_x,loot_pos_y = (1, 1)

class Loot():
    def __init__(self, loot_value=0, loot_tileset=loot_tileset, loot_pos_x=loot_pos_x, loot_pos_y=loot_pos_y):
        self.loot_value = loot_value
        self.loot_tileset = loot_tileset
        self.loot_pos_x = loot_pos_x
        self.loot_pos_y = loot_pos_y

        if self.loot_value == 10:
            self.loot_tile_x, self.loot_tile_y = (5, 8)
        elif self.loot_value == 20:
            self.loot_tile_x, self.loot_tile_y = (1, 8)
        elif self.loot_value == 30:
            self.loot_tile_x, self.loot_tile_y = (2, 8)
        else:
            self.loot_tile_x, self.loot_tile_y = (4, 8)
