import pygame
from classes.health_bar import HealthBar

character_tileset = pygame.image.load("dungeon_Resolver/dungeon_gui/assets/npc_elf.png")

TILE_SIZE = 16

class Player():
    def __init__(self, health=100, character_tileset=character_tileset, weapon=None):
        self.health = health
        self.character_tileset = character_tileset
        self.weapon = weapon
        self.player_tile_x, self.player_tile_y = (0, 0)
        self.player_pos_x, self.player_pos_y = (4.5, 5)

        # Setting up the health bar
        self.health_bar = HealthBar(max_health=health)

    def render_player(self, screen, room_x, room_y, scale_factor):
        player_surface = self.character_tileset.subsurface(pygame.Rect(self.player_tile_x * TILE_SIZE, self.player_tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        scaled_player_surface = pygame.transform.scale(player_surface, (TILE_SIZE * scale_factor, TILE_SIZE * scale_factor))
        screen.blit(scaled_player_surface, (self.player_pos_x * TILE_SIZE * scale_factor + room_x, self.player_pos_y * TILE_SIZE * scale_factor + room_y))
        
        self.weapon.render_collectable(screen, room_x + self.player_pos_x, room_y + self.player_pos_y, scale_factor - 1)

        self.health_bar.draw(screen)

    def update_room(self, room:int):
        self.room = room
    
    def travel(self, target_y):
        speed = 0.05
        self.player_pos_y -= speed

        self.weapon.pos_y -= speed + 0.015

        if self.player_pos_y < target_y:
            return True
        
    def update_health(self, health):
        self.health = health
        self.health_bar.update_health(health)