import pygame
import sys
import time
from Room import Room
from Player import Player
from Loot import Loot
# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600


# Main loop
def main():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dungeon")

    room = Room(1, True, 1, 1, 1, True, False, False, None)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))  # Fill the screen with white
        room.render_room(screen, Player(1, 100))
        pygame.display.flip()

if __name__ == "__main__":
    main()