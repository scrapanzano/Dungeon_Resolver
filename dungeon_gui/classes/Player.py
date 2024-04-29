import pygame
from classes.health_bar import HealthBar

character_tileset = pygame.image.load("dungeon_Resolver/dungeon_gui/assets/npc_elf.png")

TILE_SIZE = 16

class Player():
    def __init__(self, max_health=100, character_tileset=character_tileset, weapon=None):
        self.max_health = max_health
        self.current_health = max_health
        self.character_tileset = character_tileset
        self.weapon = weapon
        self.player_tile_x, self.player_tile_y = (0, 0)
        self.player_pos_x, self.player_pos_y = (4.5, 8)
        
        self.taking_damage = False
        self.healed = False
        self.blink_counter = 0

        # Setting up the health bar
        self.health_bar = HealthBar(blink_counter=self.blink_counter, max_health=max_health)

    def render_player(self, screen, room_x, room_y, scale_factor):
        player_surface = self.character_tileset.subsurface(pygame.Rect(self.player_tile_x * TILE_SIZE, self.player_tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        scaled_player_surface = pygame.transform.scale(player_surface, (TILE_SIZE * scale_factor, TILE_SIZE * scale_factor))
        
        if self.taking_damage and self.blink_counter % 2 == 0:
            red_surface= scaled_player_surface.copy() # Create a copy of the sprite
            red_surface.fill((255, 0, 0), special_flags=pygame.BLEND_RGBA_MULT)  # Tint the copy red
            screen.blit(red_surface, (self.player_pos_x * TILE_SIZE * scale_factor + room_x, self.player_pos_y * TILE_SIZE * scale_factor + room_y))  # Draw the tinted sprite
        elif self.healed and self.blink_counter % 2 == 0:
            green_surface= scaled_player_surface.copy() # Create a copy of the sprite
            green_surface.fill((0, 255, 0), special_flags=pygame.BLEND_RGBA_MULT)
            screen.blit(green_surface, (self.player_pos_x * TILE_SIZE * scale_factor + room_x, self.player_pos_y * TILE_SIZE * scale_factor + room_y))
        else:
            screen.blit(scaled_player_surface, (self.player_pos_x * TILE_SIZE * scale_factor + room_x, self.player_pos_y * TILE_SIZE * scale_factor + room_y))
        
        self.weapon.render_collectable(screen, room_x + self.player_pos_x, room_y + self.player_pos_y, scale_factor - 1)

        self.health_bar.draw(screen)
    
    def travel(self, target_y):
        speed = 0.05
        self.player_pos_y -= speed

        self.weapon.pos_y -= speed + 0.015

        if self.player_pos_y < target_y:
            return True
        
    def update_health(self, health):
        self.current_health = health
        self.health_bar.update_health(health)

    def get_damage(self, damage):
        new_health = self.current_health - damage
        if new_health <= 0:
            new_health = 0
            
        self.taking_damage = True
        self.update_health(new_health)
        pygame.time.set_timer(pygame.USEREVENT, 300)  # Start a timer for 300ms



    def get_heal(self, heal):
        new_health = self.current_health + heal
        if new_health > self.max_health:
            new_health = self.max_health
        
        self.healed = True
        self.update_health(new_health)
        pygame.time.set_timer(pygame.USEREVENT, 300)  # Start a timer for 300ms