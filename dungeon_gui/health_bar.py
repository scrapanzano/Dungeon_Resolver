
"""
This module is part of the dungeon_gui package, for the graphical representation of the dungeon
"""

import pygame

class HealthBar():
    """
    This class describes the representation of the Health Bar Object 
    """

    def __init__(self, blink_counter, x=50, y=130, max_health=100, current_health=100):
        self.x = x
        self.y = y
        self.max_health = max_health
        self.current_health = current_health
        self.blink_counter = blink_counter
        self.blinking = False

        self.hp_font = pygame.font.Font("dungeon_Resolver/dungeon_gui/fonts/Minecraft.ttf", 20)
        self.hp_text = self.hp_font.render(f"{self.current_health}/{self.max_health}", True, (37, 19, 26))
        self.hp_text_rect = self.hp_text.get_rect()
        center_x = 100
        center_y = 140

        self.hp_text_rect.x = center_x - self.hp_text_rect.width / 2
        self.hp_text_rect.y = (center_y - self.hp_text_rect.height / 2) + 2


    def draw(self, screen):
        """
        Draws the Health Bar Object on the screen
        
        Parameters
        ----------
        :param screen: Screen where dungeon_gui runs
        :type screen: pygame Surface
        """

        if self.blinking and self.blink_counter % 2 == 0:
            # Create a new Surface for the health bar
            health_bar_surface = pygame.Surface((self.max_health, 20))
            # Fill the Surface with the desired color
            health_bar_surface.fill((255, 100, 100))
            # Blit the Surface onto the screen with the BLEND_RGBA_MULT flag
            screen.blit(health_bar_surface, (self.x, self.y), special_flags=pygame.BLEND_RGBA_MULT)
        else:
            # Draw the background of the health bar
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.max_health, 20))
            # Draw the current health
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x, self.y, self.current_health, 20))
            # Draw the health text
            screen.blit(self.hp_text, self.hp_text_rect)


    def update_health(self, health):
        """
        Updates current_health, blinking and hp_text attributes
       
        Parameters
        ----------
        :param healt: Hero health value
        :type health: int
        """

        self.current_health = health
        self.blinking = True
        self.hp_text = self.hp_font.render(f"{self.current_health}/{self.max_health}", True, (37, 19, 26))