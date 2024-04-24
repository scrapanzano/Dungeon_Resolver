import pygame

TILE_SIZE = 16 

dungeon_tileset = pygame.image.load("dungeon_resolver/dungeon_gui/assets/dungeon_tileset.png")


# Create a list of layout for every different state of the room

room_layout = [
    "LWWWWWWWR",
    "L       R",
    "L       R",
    "L       R",
    "L       R",
    "lwwwwwwwr"
]
tile_mapping = {
    "L" : (0,0),
    "R" : (5,0), 
    "l" : (0,4),
    "r" : (5,4),
    "W" : (1,0), 
    "w" : (1,5),
    " " : (1,1)
}

class Room():
    def __init__(self, id:int, key:bool, player=None, loot=None, enemy=None, weapon=None, potion=None):
        self.id = id
        self.key = key
        self.enemy = enemy
        self.weapon = weapon
        self.player = player
        self.loot = loot
        self.potion = potion

    
    def render_room(self, screen):
        for y, row in enumerate(room_layout):
            for x, tile in enumerate(row):
                if tile in tile_mapping:
                    tile_x, tile_y = tile_mapping[tile]
                    screen.blit(dungeon_tileset, (x * TILE_SIZE, y * TILE_SIZE), (tile_x * TILE_SIZE, tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        
        if self.player is not None:
          self.player.render_player(screen)

        if self.loot is not None:
          self.loot.render_loot(screen)

        if self.potion is not None:
          self.potion.render_potion(screen)


    def add_player(self, player):
        self.player = player
        
    def remove_player(self):
        self.player = None     

    def collected_loot(self):
        self.loot = None

    def collected_potion(self):
        self.potion = None
