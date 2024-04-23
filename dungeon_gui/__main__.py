import pygame
import sys
import time
from classes.Room import Room
from classes.Player import Player
from classes.Loot import Loot
from classes.Potion import Potion
# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600


# Main loop
def main():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dungeon")

    room = Room(1, False, Player(1, 100), Loot(20), None, None, Potion(20))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))  # Fill the screen with white
        room.render_room(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()