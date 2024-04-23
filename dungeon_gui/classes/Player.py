import pygame

character_tileset = pygame.image.load("dungeon_resolver/dungeon_gui/assets/character_tileset.png")

player_tile_x, player_tile_y = (0, 0)
player_pos_x, player_pos_y = (4, 4)

class Player():
    def __init__(self, room:int, health:int, character_tileset=character_tileset, player_tile_x=player_tile_x, player_tile_y=player_tile_y, player_pos_x=player_pos_x, player_pos_y=player_pos_y):
        self.room = room
        self.health = health
        self.character_tileset = character_tileset
        self.player_tile_x = player_tile_x
        self.player_tile_y = player_tile_y
        self.player_pos_x = player_pos_x
        self.player_pos_y = player_pos_y

    def update_room(self, room:int):
        self.room = room