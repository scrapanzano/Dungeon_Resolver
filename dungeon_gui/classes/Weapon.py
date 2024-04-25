import pygame

weapon_tileset = pygame.image.load("dungeon_Resolver/dungeon_gui/assets/0x72_16x16DungeonTileset.v5.png")

TILE_SIZE_X = 16
TILE_SIZE_Y = 32


class Weapon():
    def __init__(self, damage, weapon_tileset=weapon_tileset):
        self.damage = damage
        self.weapon_tileset = weapon_tileset
        self.pos_x, self.pos_y = (1, 3)

        if self.damage == 10:
            self.loot_tile_x, self.loot_tile_y = (9, 0)
        elif self.damage == 20:
            self.loot_tile_x, self.loot_tile_y = (10, 0)
        elif self.damage == 30:
            self.loot_tile_x, self.loot_tile_y = (11, 0)
        else:
            self.loot_tile_x, self.loot_tile_y = (9, 1)

    def render_weapon(self, screen):
        screen.blit(self.weapon_tileset, (self.pos_x * TILE_SIZE_X, self.pos_y * TILE_SIZE_X), (self.loot_tile_x * TILE_SIZE_X, self.loot_tile_y * TILE_SIZE_Y, TILE_SIZE_X, TILE_SIZE_Y))