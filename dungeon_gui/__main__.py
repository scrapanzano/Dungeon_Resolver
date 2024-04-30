import pygame
import sys

from classes.player import Player
from classes.room import Room
from classes.weapon import Weapon
from classes.key import Key
from classes.loot import Loot
from classes.enemy import Enemy
from classes.potion import Potion
from classes.HUD import HUD
from classes.constants import PLAYER_GET_DAMAGE, PLAYER_GET_HEAL

# Initialize pygame
pygame.init()


# Set up the display
WIDTH, HEIGHT = 1270, 720


# Main loop
def Main():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dungeon")

    player_weapon = Weapon(damage=40, weapon_pos_x=6.8, weapon_pos_y=10)
    player = Player(max_health=100, weapon=player_weapon)

    actual_room = Room(id=0, key=Key(), loot=Loot(10), enemy=Enemy(10), weapon=Weapon(10), potion=Potion(10), has_door=True)

    actual_room.x = (WIDTH  - actual_room.width) // 2
    actual_room.y = (HEIGHT - actual_room.height) // 2

    hud = HUD()

    travel = False

    damaged = False
    healed = False

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == PLAYER_GET_DAMAGE:
                player.blink_counter += 1
                player.health_bar.blink_counter += 1
                if player.blink_counter >= 6:
                    player.taking_damage = False
                    player.health_bar.blinking = False
                    player.blink_counter = 0
                    player.health_bar.blink_counter = 0
                    pygame.time.set_timer(PLAYER_GET_DAMAGE, 0)
            if event.type == PLAYER_GET_HEAL:
                player.blink_counter += 1
                player.health_bar.blink_counter += 1
                if player.blink_counter >= 6:
                    player.taking_heal = False
                    player.health_bar.blinking = False
                    player.blink_counter = 0
                    player.health_bar.blink_counter = 0
                    pygame.time.set_timer(PLAYER_GET_HEAL, 0)

        screen.fill((37, 19, 26))  
        actual_room.render(screen)
        player.render_player(screen, actual_room.x, actual_room.y, actual_room.scale_factor)
        hud.render(screen)
        # if not healed:
        #     player.get_heal(10)
        #     healed = True
        if not damaged:
            player.get_damage(10)
            damaged = True
        pygame.display.flip()

if __name__ == "__main__":
    Main()