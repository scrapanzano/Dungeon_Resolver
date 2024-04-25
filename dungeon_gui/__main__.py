import pygame
import sys
import time
from classes.Room import Room
from classes.Player import Player
from classes.Loot import Loot
from classes.Potion import Potion
from classes.Key import Key
from classes.Weapon import Weapon
from classes.Enemy  import Enemy


# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600


# Main loop
def main():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dungeon")

    actual_room = Room(0, Player(0, 100), Key(), Loot(10), Enemy(10), Weapon(10), Potion(10))

    actual_room.x = (WIDTH  - actual_room.width) // 2
    actual_room.y = (HEIGHT - actual_room.height) // 2


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))  # Fill the screen with white
        actual_room.render_room(screen)
    
        pygame.display.flip()

if __name__ == "__main__":
    main()