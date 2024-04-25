import pygame

TILE_SIZE = 16
WIDTH, HEIGHT = 144, 112
SCALE_FACTOR = 2 

room_tileset = pygame.image.load("dungeon_resolver/dungeon_gui/assets/dungeon_tileset.png")


# Create a list of layout for every different state of the room

room_layout = [
    "LWWWWWWWR",
    "L       R",
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
    def __init__(self, id:int, player=None, key= None, loot=None, enemy=None, weapon=None, potion=None, width=WIDTH, height=HEIGHT, x=0, y=0):
        self.id = id
        self.player = player
        self.key = key
        self.loot = loot
        self.enemy = enemy
        self.weapon = weapon
        self.potion = potion
        self.width = WIDTH
        self.height = HEIGHT
        self.x = x
        self.y = y

        self.surface = pygame.Surface((self.width, self.height))

    
    def render_room(self, screen):
        for y, row in enumerate(room_layout):
            for x, tile in enumerate(row):
                if tile in tile_mapping:
                    tile_x, tile_y = tile_mapping[tile]
                    self.surface.blit(room_tileset, (x * TILE_SIZE, y * TILE_SIZE), (tile_x * TILE_SIZE, tile_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        
         # Scale the surface
        scaled_surface = pygame.transform.scale(self.surface, (self.width * SCALE_FACTOR, self.height * SCALE_FACTOR))

        # Calculate the new position of the room to center it
        screen_width, screen_height = pygame.display.get_surface().get_size()
        self.x = (screen_width - self.width * SCALE_FACTOR) // 2
        self.y = (screen_height - self.height * SCALE_FACTOR) // 2

        # Draw the scaled surface onto the screen
        screen.blit(scaled_surface, (self.x, self.y))

        if self.player is not None:
          self.player.render_player(screen, self.x, self.y, SCALE_FACTOR)

        if self.key is not None:
            self.key.render_key(screen, self.x, self.y, SCALE_FACTOR)

        if self.loot is not None:
          self.loot.render_loot(screen, self.x, self.y, SCALE_FACTOR)

        if self.enemy is not None:
          self.enemy.render_enemy(screen, self.x, self.y, SCALE_FACTOR)

        if self.weapon is not None:
            self.weapon.render_weapon(screen, self.x, self.y, SCALE_FACTOR)

        if self.potion is not None:
          self.potion.render_potion(screen, self.x, self.y, SCALE_FACTOR)


    def add_player(self, player):
        self.player = player
        
    def remove_player(self):
        self.player = None 

    def add_key(self, key):
        self.key = key

    def remove_key(self):
        self.key = None    

    def add_loot(self, loot):
        self.loot = loot

    def remove_loot(self):
        self.loot = None
    
    def add_potion(self, potion):
        self.potion = potion

    def remove_potion(self):
        self.potion = None

    def add_weapon(self, weapon):
        self.weapon = weapon
    
    def remove_weapon(self):
        self.weapon = None
    
    def add_enemy(self, enemy):
        self.enemy = enemy
    
    def remove_enemy(self):
        self.enemy = None

    
