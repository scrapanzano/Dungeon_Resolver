import pygame
import sys
import time
from classes.room import Room
from classes.player import Player
from classes.loot import Loot
from classes.potion import Potion
from classes.key import Key
from classes.weapon import Weapon
from classes.enemy  import Enemy


# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1270, 720


# Main loop
def main():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dungeon")

    actual_room = Room(id=0, player=Player(0, 100), key=Key(), loot=Loot(10), enemy=Enemy(10), weapon=Weapon(10), potion=Potion(10), has_door=False)

    actual_room.x = (WIDTH  - actual_room.width) // 2
    actual_room.y = (HEIGHT - actual_room.height) // 2


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  
        actual_room.render_room(screen)
    
        pygame.display.flip()

if __name__ == "__main__":
    main()