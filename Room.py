"""
This module is part of the dungeon_gui package, for the graphical representation of the dungeon
"""

import pygame

TILE_SIZE = 16
WIDTH, HEIGHT = 160, 176
SCALE_FACTOR = 4 

room_tileset = pygame.image.load("dungeon_resolver/dungeon_gui/assets/dungeon_tileset.png")


# Create a list of layout for every different state of the room

# room_layout = [
#     "....  ....",
#     "....  ....",
#     "LWWTDdTWWR",
#     "L        R",
#     "L        R",
#     "L        R",
#     "L        R",
#     "L        R",
#     "lwww  wwwr",
#     "....  ....",
#     "....  ....",
# ]

room_layout = [
    "...L  R...",
    "...L  R...",
    "LWWTDdTWWR",
    "L        R",
    "L        R",
    "L        R",
    "L        R",
    "L        R",
    "L        R",
    "lwwC  cwwr",
    "...L  R...",
    "...L  R...",
]


class Room():
    """
    This class describes the representation of the Room 
    """
    def __init__(self, id:int, key= None, loot=None, enemy=None, weapon=None, potion=None, width=WIDTH, height=HEIGHT, has_door = False, x=0, y=0):
        self.id = id
        self.key = key
        self.loot = loot
        self.enemy = enemy
        self.weapon = weapon
        self.potion = potion
        self.width = WIDTH
        self.height = HEIGHT
        self.has_door = has_door
        self.x = x
        self.y = y
        self.scale_factor = SCALE_FACTOR
        self.tile_mapping = self.generate_tile_mapping()

        self.collectables = [key, loot, weapon, potion]


        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((37, 19, 26))
    

    def render(self, screen):
        """
        Rendering of the Room Object on the screen using a tile set

        Parameters
        ---------- 
        :param screen: Screen where dungeon_gui runs
        :type screen: pygame Surface
        """
        for y, row in enumerate(room_layout):
            for x, tile in enumerate(row):
                if tile in self.tile_mapping:
                    tile_x, tile_y = self.tile_mapping[tile]
                    if tile == 'T':
                        # Render tile 'W' first
                        tile_w_x, tile_w_y = self.tile_mapping['W']
                        self.surface.blit(room_tileset, (x * TILE_SIZE, y * TILE_SIZE), (tile_w_x * TILE_SIZE, tile_w_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                        # Then render tile 'T' above it
                        self.surface.blit(room_tileset, (x * TILE_SIZE, y * TILE_SIZE), (tile_x * TILE_SIZE, tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                    elif tile == 'D' or tile == 'd':
                        # Render tile ' ' first
                        tile_space_x, tile_space_y = self.tile_mapping[' ']
                        self.surface.blit(room_tileset, (x * TILE_SIZE, y * TILE_SIZE), (tile_space_x * TILE_SIZE, tile_space_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                        # Then render tile 'C' above it
                        self.surface.blit(room_tileset, (x * TILE_SIZE, y * TILE_SIZE), (tile_x * TILE_SIZE, tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                    else:
                        # Render other tiles normally
                        self.surface.blit(room_tileset, (x * TILE_SIZE, y * TILE_SIZE), (tile_x * TILE_SIZE, tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        # Scale the surface
        scaled_surface = pygame.transform.scale(self.surface, (self.width * self.scale_factor, self.height * self.scale_factor))

        # Calculate the new position of the room to center it
        screen_width, screen_height = pygame.display.get_surface().get_size()
        self.x = (screen_width - self.width * self.scale_factor) // 2
        self.y = (screen_height - self.height * self.scale_factor) // 2

        # Draw the scaled surface onto the screen
        screen.blit(scaled_surface, (self.x, self.y))


        for collectable in self.collectables:
            if collectable is not None:
                collectable.render_collectable(screen, self.scale_factor)

        if self.enemy is not None:
          self.enemy.render_enemy(screen, self.x, self.y, self.scale_factor)


    def generate_tile_mapping(self):
        """
        Generates a tile mapping for the room representation
        
        Returns
        -------
        :returns: A dict containing the tile mapping
        :rtype: dict
        """
        # tile_mapping = {
        #     "L" : (0,0),
        #     "R" : (5,0), 
        #     "l" : (0,4),
        #     "r" : (5,4),
        #     "W" : (1,0), 
        #     "w" : (1,5),
        #     "T" : (0,9),
        #     "D" : (6,6) if self.has_door else (1,1),
        #     "d" : (7,6) if self.has_door else (1,1),
        #     " " : (1,1)
        # }

        tile_mapping = {
            "L" : (0,0),
            "R" : (5,0), 
            "l" : (0,4),
            "r" : (5,4),
            "W" : (1,0), 
            "w" : (1,5),
            "C" : (3,5),
            "c" : (0,5),
            "T" : (0,9),
            "D" : (6,6) if self.has_door else (1,1),
            "d" : (7,6) if self.has_door else (1,1),
            " " : (1,1)
        }

        return tile_mapping


    def collect_key(self):
        """
        Calls the function to set key's collected attribute
        """
        if self.key is not None:
            self.key.collect()
            self.key = None
        

    def collect_treasure(self):
        """
        Calls the function to set treasure's collected attribute
        """        
        if self.loot is not None:
            self.loot.collect()
            self.loot = None


    def collect_weapon(self):
        """
        Calls the function to set weapon's collected attribute
        """        
        if self.weapon is not None:
            self.weapon.collect()
            self.weapon = None


    def collect_potion(self):
        """
        Calls the function to set potion's collected attribute
        """
        if self.potion is not None:
            self.potion.collect()
            self.potion = None


    def defeat_enemy(self):
        """
        Calls the function to set enemy's killed attribute
        """
        if self.enemy is not None:
            self.enemy.kill()
            if self.enemy.alpha <= 0:
                self.enemy = None
    

    def set_key(self, key):
        """
        Sets the value of key

        Parameters
        ----------
        :param key: Key Object to set
        :type key: Key
        """
        self.key = key


    def set_loot(self, loot):
        """
        Sets the value of loot

        Parameters
        ----------
        :param loot: Loot Object to set
        :type loot: Loot
        """
        self.loot = loot


    def set_enemy(self, enemy):
        """
        Sets the value of enemy

        Parameters
        ----------
        :param enemy: Enemy Object to set
        :type enemy: Enemy
        """
        self.loot = enemy


    def set_weapon(self, weapon):
        """
        Sets the value of weapon

        Parameters
        ----------
        :param weapon: Weapon Object to set
        :type weapon: Weapon
        """
        self.weapon = weapon
    

    def set_potion(self, potion):
        """
        Sets the value of potion

        Parameters
        ----------
        :param potion: Potion Object to set
        :type potion: Potion
        """
        self.potion = potion