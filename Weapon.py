import pygame

from collectable import Collectable

weapon_tileset = pygame.image.load("dungeon_Resolver/dungeon_gui/assets/0x72_16x16DungeonTileset.v5.png")

TILE_SIZE_X = 16
TILE_SIZE_Y = 32

WEAPON_START_ENTER_POS = (13.5, 18.5)
WEAPON_ENTER_ENDING_POS = (13.5, 10.5)

SPEED = 0.03

class Weapon(Collectable):
    def __init__(self, damage=0, weapon_tileset=weapon_tileset, weapon_pos_x=WEAPON_START_ENTER_POS[0], weapon_pos_y=WEAPON_START_ENTER_POS[1]):
        super().__init__()
        self.weapon_tileset = weapon_tileset
        self.pos_x = weapon_pos_x
        self.pos_y = weapon_pos_y
        self.target_y = weapon_pos_y

        self.visible = False

        self.update_damage(damage)

    def render_collectable(self, screen, scale_factor):
        if self.visible:
            weapon_surface = self.weapon_tileset.subsurface(pygame.Rect(self.weapon_tile_x * TILE_SIZE_X, self.weapon_tile_y * TILE_SIZE_Y, TILE_SIZE_X, TILE_SIZE_Y))
            scaled_weapon_surface = pygame.transform.scale(weapon_surface, (TILE_SIZE_X * (scale_factor - 1), TILE_SIZE_Y * (scale_factor - 1)))
        
            if self.collected and self.alpha > 0:
                self.alpha -= 8
                scaled_weapon_surface.set_alpha(self.alpha)
            elif self.alpha <= 0:
                return
        
            screen.blit(scaled_weapon_surface, (self.pos_x * TILE_SIZE_X * scale_factor, self.pos_y * TILE_SIZE_X * scale_factor))

    def move(self, target_y):
        self.target_y = target_y
    
    def update(self):
        self.pos_y = pygame.math.lerp(self.pos_y, self.target_y, SPEED)
        if abs(self.pos_y - self.target_y) < 0.01:
            self.pos_y = self.target_y

    def update_damage(self, damage):
        self.damage = damage

        if self.damage == 30:
            self.weapon_tile_x, self.weapon_tile_y = (9, 0)
            self.visible = True
        elif self.damage == 50:
            self.weapon_tile_x, self.weapon_tile_y = (10, 0)
            self.visible = True
        elif self.damage == 70:
            self.weapon_tile_x, self.weapon_tile_y = (11, 0)
            self.visible = True
        elif self.damage == 90:
            self.weapon_tile_x, self.weapon_tile_y = (9, 1)
            self.visible = True
        else :
            self.visible = False  