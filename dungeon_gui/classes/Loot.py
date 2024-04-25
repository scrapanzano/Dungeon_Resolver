import pygame

loot_tileset = pygame.image.load("dungeon_resolver/dungeon_gui/assets/dungeon_tileset.png")

TILE_SIZE = 16

class Loot():
    def __init__(self, loot_value:int, loot_tileset=loot_tileset):
        self.loot_value = loot_value
        self.loot_tileset = loot_tileset
        self.loot_pos_x, self.loot_pos_y = (1, 1)

        if self.loot_value == 10:
            self.loot_tile_x, self.loot_tile_y = (5, 8)
        elif self.loot_value == 20:
            self.loot_tile_x, self.loot_tile_y = (1, 8)
        elif self.loot_value == 30:
            self.loot_tile_x, self.loot_tile_y = (2, 8)
        else:
            self.loot_tile_x, self.loot_tile_y = (4, 8)

    def render_loot(self, screen):
        screen.blit(self.loot_tileset, (self.loot_pos_x * TILE_SIZE, self.loot_pos_y * TILE_SIZE), (self.loot_tile_x * TILE_SIZE, self.loot_tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))