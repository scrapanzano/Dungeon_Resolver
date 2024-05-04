
"""
This module is part of the dungeon_gui package, for the graphical representation of the dungeon
"""

import pygame

TILE_SIZE = 16
SCALE_FACTOR = 2

FONT_PATH = "dungeon_Resolver/dungeon_gui/fonts/Minecraft.ttf"

class HUD():
    """
    This class describes the representation of the HUD 
    """
    def __init__(self, hero_loot=0, hero_loot_goal=0, key_counter=0, potion_counter=0, room_id=0, defeated_enemy_counter=0, defeated_enemy_counter_goal=0, action=""):

        # Setting up the hero loot HUD
        self.hero_loot = hero_loot
        self.hero_loot_goal = hero_loot_goal
        self.font = pygame.font.Font(FONT_PATH, 36)
        self.loot_text = self.font.render(f"Loot: {self.hero_loot}/{self.hero_loot_goal}", True, (255, 255, 255))
        self.loot_text_rect = self.loot_text.get_rect()
        self.loot_text_rect.x = 50
        self.loot_text_rect.y = 130

        loot_tile_x = 6
        loot_tile_y = 8

        loot_pixel_x = loot_tile_x * TILE_SIZE
        loot_pixel_y = loot_tile_y * TILE_SIZE


        self.loot_icon = pygame.image.load("dungeon_Resolver/dungeon_gui/assets/dungeon_tileset.png")
        self.loot_icon = self.loot_icon.subsurface(pygame.Rect(loot_pixel_x, loot_pixel_y, TILE_SIZE, TILE_SIZE))
        self.loot_icon = pygame.transform.scale(self.loot_icon, (40, 40))
        
        self.loot_icon_rect = self.loot_icon.get_rect()
        self.loot_icon_rect.x = 5
        self.loot_icon_rect.y = self.loot_text_rect.y - 7.5

        # Setting up the keys HUD
        self.keys = key_counter
        self.keys_text = self.font.render(f"Keys: {self.keys}", True, (255, 255, 255))
        self.keys_text_rect = self.keys_text.get_rect()
        self.keys_text_rect.x = 50
        self.keys_text_rect.y = 50

        keys_tile_x = 9
        keys_tile_y = 9

        keys_pixel_x = keys_tile_x * TILE_SIZE
        keys_pixel_y = keys_tile_y * TILE_SIZE

        self.keys_icon = pygame.image.load("dungeon_Resolver/dungeon_gui/assets/dungeon_tileset.png")
        self.keys_icon = self.keys_icon.subsurface(pygame.Rect(keys_pixel_x, keys_pixel_y, TILE_SIZE, TILE_SIZE))
        self.keys_icon = pygame.transform.scale(self.keys_icon, (40, 40))

        self.keys_icon_rect = self.keys_icon.get_rect()
        self.keys_icon_rect.x = 5
        self.keys_icon_rect.y = self.keys_text_rect.y - 7.5

        # Setting up the potions HUD
        self.potions = potion_counter
        self.potions_text = self.font.render(f"Potions: {self.potions}", True, (255, 255, 255))
        self.potions_text_rect = self.potions_text.get_rect()
        self.potions_text_rect.x = 50
        self.potions_text_rect.y = 90

        potions_tile_x = 12
        potions_tile_y = 11

        potions_pixel_x = potions_tile_x * TILE_SIZE
        potions_pixel_y = potions_tile_y * TILE_SIZE

        self.potions_icon = pygame.image.load("dungeon_Resolver/dungeon_gui/assets/0x72_16x16DungeonTileset.v5.png")
        self.potions_icon = self.potions_icon.subsurface(pygame.Rect(potions_pixel_x, potions_pixel_y, TILE_SIZE, TILE_SIZE))
        self.potions_icon = pygame.transform.scale(self.potions_icon, (40, 40))

        self.potions_icon_rect = self.potions_icon.get_rect()
        self.potions_icon_rect.x = 5
        self.potions_icon_rect.y = self.potions_text_rect.y - 7.5

        # Setting up the health icon HUD
        self.health_icon = pygame.image.load("dungeon_Resolver/dungeon_gui/assets/Sprite_heart.png")
        self.health_icon = self.health_icon.subsurface(pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE))
        self.health_icon = pygame.transform.scale(self.health_icon, (30, 30))

        self.health_icon_rect = self.health_icon.get_rect()
        self.health_icon_rect.x = 10
        self.health_icon_rect.y = 170 - 7.5

        # Setting up the room id HUD
        self.id_font = pygame.font.Font(FONT_PATH, 250)
        self.id = room_id
        self.id_text = self.id_font.render(f"{self.id}", True, (255, 255, 255))

        # Create a new surface with the same size as the id_text
        self.id_text_alpha = pygame.Surface(self.id_text.get_size(), pygame.SRCALPHA)

        # Fill the new surface with the desired color
        self.id_text_alpha.fill((255, 255, 255))

        # Set the alpha of the new surface
        self.id_text_alpha.set_alpha(100)  # Set the alpha to a low value to make the text barely visible

        # Blit the id_text onto the new surface with a blending mode
        self.id_text_alpha.blit(self.id_text, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        self.id_text_rect = self.id_text.get_rect()
        center_x = 1100
        center_y = 400
        self.id_text_rect.x = center_x - self.id_text_rect.width / 2
        self.id_text_rect.y = center_y - self.id_text_rect.height / 2

        # Setting up the defeated enemy counter HUD
        self.defeated_enemy_counter = defeated_enemy_counter
        self.defeated_enemy_counter_goal = defeated_enemy_counter_goal
        self.defeated_enemy_counter_text = self.font.render(f"Defeated Enemies: {self.defeated_enemy_counter}/{self.defeated_enemy_counter_goal}", True, (255, 255, 255))
        self.defeated_enemy_counter_text_rect = self.defeated_enemy_counter_text.get_rect()
        self.defeated_enemy_counter_text_rect.x = 50
        self.defeated_enemy_counter_text_rect.y = 10

        enemies_tile_x = 1
        enemies_tile_y = 3

        enemies_pixel_x = enemies_tile_x * TILE_SIZE
        enemies_pixel_y = enemies_tile_y * TILE_SIZE

        self.enemy_icon = pygame.image.load("dungeon_Resolver/dungeon_gui/assets/0x72_16x16DungeonTileset.v5.png")
        self.enemy_icon = self.enemy_icon.subsurface(pygame.Rect(enemies_pixel_x, enemies_pixel_y, TILE_SIZE, TILE_SIZE))
        self.enemy_icon = pygame.transform.scale(self.enemy_icon, (40, 40))
        
        self.enemy_icon_rect = self.enemy_icon.get_rect()
        self.enemy_icon_rect.x = 5
        self.enemy_icon_rect.y = self.defeated_enemy_counter_text_rect.y - 7.5

        
        # Setting up the action text HUD
        self.action = action
        self.action_font = pygame.font.Font(FONT_PATH, 36)
        self.action_text = self.action_font.render(f"{self.action}", True, (255, 255, 255))
        self.action_text_rect = self.action_text.get_rect()
        self.action_text_rect.x = 20
        self.action_text_rect.y = 660


    def render(self, screen):
        """
        Rendering all HUD Object elements on the screen using a tile set
        
        Parameters
        ----------
        :param screen: Screen where dungeon_gui runs
        :type screen: pygame Surface
        """

        screen.blit(self.loot_icon, self.loot_icon_rect)
        screen.blit(self.keys_icon, self.keys_icon_rect)
        screen.blit(self.potions_icon, self.potions_icon_rect)
        screen.blit(self.health_icon, self.health_icon_rect)
        screen.blit(self.enemy_icon, self.enemy_icon_rect)
        screen.blit(self.loot_text, self.loot_text_rect)
        screen.blit(self.keys_text, self.keys_text_rect)
        screen.blit(self.potions_text, self.potions_text_rect)
        screen.blit(self.defeated_enemy_counter_text, self.defeated_enemy_counter_text_rect)
        screen.blit(self.id_text_alpha, self.id_text_rect)
        screen.blit(self.action_text, self.action_text_rect)
          
    def update_hero_loot(self, hero_loot):
        """
        Updates hero_loot attribute and its HUD representation
       
        Parameters
        ----------
        :param hero_loot: Hero loot value
        :type hero_loot: int
        """
        self.hero_loot = hero_loot
        self.loot_text = self.font.render(f"Loot: {self.hero_loot}/{self.hero_loot_goal}", True, (255, 255, 255))


    def update_keys(self, keys):
        """
        Updates keys attribute and its HUD representation
       
        Parameters
        ----------
        :param keys: Number of keys owned
        :type keys: int
        """
        self.keys = keys
        self.keys_text = self.font.render(f"Keys: {self.keys}", True, (255, 255, 255))


    def update_potions(self, potions):
        """
        Updates potions attribute and its HUD representation
       
        Parameters
        ----------
        :param potions: Number of potions owned
        :type potions: int
        """
        self.potions = potions
        self.potions_text = self.font.render(f"Potions: {self.potions}", True, (255, 255, 255))

    def update_defeated_enemy_counter(self, defeated_enemy_counter):
        """
        Updates defeated_enemy_counter attribute and its HUD representation
       
        Parameters
        ----------
        :param defeated_enemy_counter: Number of defeated enemies
        :type defeated_enemy_counter: int
        """
        self.defeated_enemy_counter = defeated_enemy_counter
        self.defeated_enemy_counter_text = self.font.render(f"Defeated Enemies: {self.defeated_enemy_counter}/{self.defeated_enemy_counter_goal}", True, (255, 255, 255))
    

    def create_alpha_surface(self, text_surface, alpha_value):
        """
        Creates an alpha surface for HUD id representation

        Parameters
        ----------
        :param text_surface: Text Surface
        :type text_surface: pygame Surface
        :param alpha_value: Alpha value for the Surface
        :type alpha_value: int
        
        Returns
        -------
        :returns: A Surface for the room id in HUD 
        :rtype: pygame Surface
        """

        # Create a new surface with the same size as the text_surface
        alpha_surface = pygame.Surface(text_surface.get_size(), pygame.SRCALPHA)
    
        # Fill the new surface with the desired color
        alpha_surface.fill((255, 255, 255))
    
        # Set the alpha of the new surface
        alpha_surface.set_alpha(alpha_value)  # Set the alpha to a low value to make the text barely visible
    
        # Blit the text_surface onto the new surface with a blending mode
        alpha_surface.blit(text_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    
        return alpha_surface

    def update_id(self, new_id):
        """
        Updates id attribute and its HUD representation
       
        Parameters
        ----------
        :param new_id: Number of room visited
        :type new_id: int
        """        

        self.id = new_id
        self.id_text = self.id_font.render(f"{self.id}", True, (255, 255, 255))
        self.id_text_alpha = self.create_alpha_surface(self.id_text, 100)
    
        self.id_text_rect = self.id_text.get_rect()
        center_x = 1100
        center_y = 400
        self.id_text_rect.x = center_x - self.id_text_rect.width / 2
        self.id_text_rect.y = center_y - self.id_text_rect.height / 2
 

    def update_action(self, action):
        self.action = action
        self.action_text = self.action_font.render(f"{self.action}", True, (255, 255, 255))
