import pygame
import sys
from classes.room import Room
from classes.player import Player
from classes.loot import Loot
from classes.potion import Potion
from classes.key import Key
from classes.weapon import Weapon
from classes.enemy  import Enemy
from classes.hud import HUD

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1270, 720


# Main loop
def main():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dungeon")

    player_weapon = Weapon(damage=10, weapon_pos_x=6.8, weapon_pos_y=6)
    player = Player(health=100, weapon=player_weapon)

    actual_room = Room(id=0, player=player, key=Key(), loot=Loot(10), enemy=Enemy(10), weapon=Weapon(10), potion=Potion(10), has_door=False)

    actual_room.x = (WIDTH  - actual_room.width) // 2
    actual_room.y = (HEIGHT - actual_room.height) // 2

    hud = HUD()

    travel = False

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  
        actual_room.render(screen)
        player.render_player(screen, actual_room.x, actual_room.y, actual_room.scale_factor)
        hud.render(screen)
        if not travel:
            travel = player.travel(0)
        pygame.display.flip()

if __name__ == "__main__":
    main()