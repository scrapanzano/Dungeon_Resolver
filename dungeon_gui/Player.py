
"""
This module is part of the dungeon_gui package, for the graphical representation of the dungeon
"""

import pygame
from dungeon_gui.health_bar import HealthBar
from dungeon_gui.constants import PLAYER_GET_DAMAGE, PLAYER_GET_HEAL, PLAYER_ENTER_ENDING_POS, PLAYER_ENTER_STARTING_POS


character_tileset = pygame.image.load("dungeon_Resolver/dungeon_gui/assets/npc_elf.png")

TILE_SIZE = 16


class Player():
    """
    This class describes the representation of the Hero Player 
    """    

    def __init__(self, current_health=100, max_health=100, pos_x=PLAYER_ENTER_ENDING_POS[0], pos_y=PLAYER_ENTER_ENDING_POS[1], character_tileset=character_tileset, weapon=None, potion = None):
        self.current_health = current_health
        self.max_health = max_health
        self.character_tileset = character_tileset
        self.weapon = weapon
        self.potion = potion
        self.player_tile_x, self.player_tile_y = (0, 0)
        self.player_pos_x = pos_x
        self.player_pos_y = pos_y
        self.target_y = pos_y
        
        self.taking_damage = False
        self.taking_heal = False
        self.blink_counter = 0

        self.is_moving = False

        # Setting up the health bar
        self.health_bar = HealthBar(blink_counter=self.blink_counter, max_health=self.max_health, current_health=self.current_health)

    def render_player(self, screen, scale_factor):
        """
        Rendering of the Player Object on the screen using a tile set

        Parameters
        ---------- 
        :param screen: Screen where dungeon_gui runs
        :type screen: pygame Surface
        :param scale_factor: Object scale factor 
        :type scale_factor: int
        """

        player_surface = self.character_tileset.subsurface(pygame.Rect(self.player_tile_x * TILE_SIZE, self.player_tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        scaled_player_surface = pygame.transform.scale(player_surface, (TILE_SIZE * scale_factor, TILE_SIZE * scale_factor))
        
        if self.taking_damage and self.blink_counter % 2 == 0:
            red_surface= scaled_player_surface.copy() # Create a copy of the sprite
            red_surface.fill((255, 0, 0), special_flags=pygame.BLEND_RGBA_MULT)  # Tint the copy red
            screen.blit(red_surface, (self.player_pos_x * TILE_SIZE * scale_factor, self.player_pos_y * TILE_SIZE * scale_factor))  # Draw the tinted sprite
        elif self.taking_heal and self.blink_counter % 2 == 0:
            green_surface= scaled_player_surface.copy() # Create a copy of the sprite
            green_surface.fill((0, 255, 0), special_flags=pygame.BLEND_RGBA_MULT)
            screen.blit(green_surface, (self.player_pos_x * TILE_SIZE * scale_factor, self.player_pos_y * TILE_SIZE * scale_factor))
        else:
            screen.blit(scaled_player_surface, (self.player_pos_x * TILE_SIZE * scale_factor, self.player_pos_y * TILE_SIZE * scale_factor))

        self.health_bar.draw(screen)


    def update_health(self, health):
        """
        Updates current_health attribute and health_bar
       
        Parameters
        ----------
        :param health: Hero healt value
        :type health: int
        """
        self.current_health = health
        self.health_bar.update_health(health)


    def get_damage(self, damage):
        """
        Manages the damage taken by the hero, updating his health
       
        Parameters
        ----------
        :param damage: Damage value
        :type damage: int
        """

        new_health = self.current_health - damage
        if new_health <= 0:
            new_health = 0
            
        self.taking_damage = True
        self.update_health(new_health)
        pygame.time.set_timer(PLAYER_GET_DAMAGE, 300)  # Start a timer for 300ms


    def get_heal(self):
        """
        Manages the hero's health, when healing himself
       
        Parameters
        ----------
        :param heal: Heal value
        :type heal: int
        """

        new_health = self.current_health + self.potion.potion_value
        if new_health > self.max_health:
            new_health = self.max_health
        
        self.taking_heal = True
        self.update_health(new_health)
        pygame.time.set_timer(PLAYER_GET_HEAL, 300)  # Start a timer for 300ms

    def update_weapon(self, new_damage):
        """
        Calls the function to update the weapon's damage
       
        Parameters
        ----------
        :param new_damage: Weapon damage value
        :type new_damage: int
        """

        self.weapon.update_damage(new_damage)

    def collect_potion(self, potion):
        """
        Calls the function to collect the potion
       
        Parameters
        ----------
        :param potion: Potion object
        :type potion: Potion
        """

        self.potion = potion