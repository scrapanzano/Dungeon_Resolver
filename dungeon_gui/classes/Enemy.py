import pygame

enemy_tileset = pygame.image.load("dungeon_Resolver/dungeon_gui/assets/0x72_16x16DungeonTileset.v5.png")

TILE_SIZE = 16

class Enemy():
    def __init__(self, damage, enemy_tileset=enemy_tileset):
        self.enemy_tileset = enemy_tileset
        self.damage = damage
        self.enemy_tileset = enemy_tileset
        self.pos_x, self.pos_y = (4, 3)

        if self.damage == 10:
            self.enemy_tile_x, self.enemy_tile_y = (0, 12)
        elif self.damage == 20:
            self.enemy_tile_x, self.enemy_tile_y = (1, 12)
        elif self.damage == 30:
            self.enemy_tile_x, self.enemy_tile_y = (2, 12)
        else:
            self.enemy_tile_x, self.enemy_tile_y = (3, 12)

    def render_enemy(self, screen):
        screen.blit(self.enemy_tileset, (self.pos_x * TILE_SIZE, self.pos_y * TILE_SIZE), (self.enemy_tile_x * TILE_SIZE, self.enemy_tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))