import pygame
from .health_bar import HealthBar

TILE_SIZE = 16
SCALE_FACTOR = 2

class HUD():
    def __init__(self, hero_loot=0, keys=0, potions=0):
        # Setting up the hero loot HUD
        self.hero_loot = hero_loot
        self.font = pygame.font.Font("dungeon_Resolver/dungeon_gui/Minecraft.ttf", 36)
        self.loot_text = self.font.render(f"Loot: {self.hero_loot}", True, (255, 255, 255))
        self.loot_text_rect = self.loot_text.get_rect()
        self.loot_text_rect.x = 50
        self.loot_text_rect.y = 10

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
        self.keys = keys
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
        self.potions = potions
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

        # Setting up the health bar
        self.health_icon = pygame.image.load("dungeon_Resolver/dungeon_gui/assets/HeartUiFull.png")

        # self.health_bar = HealthBar()

    def render(self, screen):
        screen.blit(self.loot_icon, self.loot_icon_rect)
        screen.blit(self.keys_icon, self.keys_icon_rect)
        screen.blit(self.potions_icon, self.potions_icon_rect)
        screen.blit(self.loot_text, self.loot_text_rect)
        screen.blit(self.keys_text, self.keys_text_rect)
        screen.blit(self.potions_text, self.potions_text_rect)
        # self.health_bar.draw(screen)


    def update(self, hero_loot):
        self.hero_loot = hero_loot
        self.loot_text = self.font.render(f"Loot: {self.hero_loot}", True, (255, 255, 255))
    
    def update_keys(self, keys):
        self.keys = keys
        self.keys_text = self.font.render(f"Keys: {self.keys}", True, (255, 255, 255))

    def update_potions(self, potions):
        self.potions = potions
        self.potions_text = self.font.render(f"Potions: {self.potions}", True, (255, 255, 255))