import pygame

character_tileset = pygame.image.load("dungeon_Resolver/dungeon_gui/assets/npc_elf.png")

TILE_SIZE = 16

class Player():
    def __init__(self, room:int, health:int, character_tileset=character_tileset):
        self.room = room
        self.health = health
        self.character_tileset = character_tileset
        self.player_tile_x, self.player_tile_y = (0, 0)
        self.player_pos_x, self.player_pos_y = (4.5, 5)

    def render_player(self, screen, room_x, room_y, scale_factor):
        player_surface = self.character_tileset.subsurface(pygame.Rect(self.player_tile_x * TILE_SIZE, self.player_tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        scaled_player_surface = pygame.transform.scale(player_surface, (TILE_SIZE * scale_factor, TILE_SIZE * scale_factor))
        screen.blit(scaled_player_surface, (self.player_pos_x * TILE_SIZE * scale_factor + room_x, self.player_pos_y * TILE_SIZE * scale_factor + room_y))

    def update_room(self, room:int):
        self.room = room
    
    def travel(self, target_y):
        self.player_pos_y -= 0.1
        pygame.time.delay(60)
        if self.player_pos_y < target_y:
            return True