import pygame

TILE_SIZE = 16
WIDTH, HEIGHT = 160, 112
SCALE_FACTOR = 2 

room_tileset = pygame.image.load("dungeon_resolver/dungeon_gui/assets/dungeon_tileset.png")


# Create a list of layout for every different state of the room

room_layout = [
    "LWWWDdWWWR",
    "L        R",
    "L        R",
    "L        R",
    "L        R",
    "L        R",
    "lwww  wwwwr"
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
    def __init__(self, id:int, player=None, key= None, loot=None, enemy=None, weapon=None, potion=None, width=WIDTH, height=HEIGHT, has_door = False, x=0, y=0):
        self.id = id
        self.player = player
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

        self.collectables = [key, loot, weapon, potion]

        tile_mapping.update({
            "D" : (6,6) if has_door else (1,1),
            "d" : (7,6) if has_door else (1,1)
        })

        self.surface = pygame.Surface((self.width, self.height))

    
    def render(self, screen):
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

        for collectable in self.collectables:
            if collectable is not None:
                collectable.render_collectable(screen, self.x, self.y, SCALE_FACTOR)

        if self.enemy is not None:
          self.enemy.render_enemy(screen, self.x, self.y, SCALE_FACTOR)

        if self.player is not None:
          self.player.render_player(screen, self.x, self.y, SCALE_FACTOR)


    def collect_key(self):
        if self.key is not None:
            self.key.collect()
            self.key = None
        

    def collect_loot(self):
        if self.loot is not None:
            self.loot.collect()
            self.loot = None

    def collect_weapon(self):
        if self.weapon is not None:
            self.weapon.collect()
            self.weapon = None

    def collect_potion(self):
        if self.potion is not None:
            self.potion.collect()
            self.potion = None

    def kill_enemy(self):
        if self.enemy is not None:
            self.enemy.kill()
            if self.enemy.alpha <= 0:
                self.enemy = None
    