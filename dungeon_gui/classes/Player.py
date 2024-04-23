import pygame

character_tileset = pygame.image.load("dungeon_resolver/dungeon_gui/assets/character_tileset.png")



class Player():
    def __init__(self, room:int, health:int, character_tileset=character_tileset):
        self.room = room
        self.health = health
        self.character_tileset = character_tileset
        self.player_tile_x, self.player_tile_y = (0, 0)
        self.player_pos_x, self.player_pos_y = (4, 4)

    def update_room(self, room:int):
        self.room = room