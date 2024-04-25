import pygame

character_tileset = pygame.image.load("dungeon_Resolver/dungeon_gui/assets/npc_elf.png")

TILE_SIZE = 16

class Player():
    def __init__(self, room:int, health:int, character_tileset=character_tileset):
        self.room = room
        self.health = health
        self.character_tileset = character_tileset
        self.player_tile_x, self.player_tile_y = (0, 0)
        self.player_pos_x, self.player_pos_y = (4, 5)

    def render_player(self, screen, room_x, room_y):
        screen.blit(self.character_tileset, (self.player_pos_x * TILE_SIZE + room_x, self.player_pos_y * TILE_SIZE + room_y), (self.player_tile_x * TILE_SIZE, self.player_tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def update_room(self, room:int):
        self.room = room