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
import networkx as nx

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600


# Main loop
def main():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dungeon")

    room1 = Room(0, 0, 0, Player(1, 100), Key(), Loot(10), Enemy(10), Weapon(10), Potion(10))
    room2 = Room(1, 0, 0, None, Key(), Loot(10), Enemy(10), Weapon(10), Potion(10))
    room3 = Room(2, 0, 0, None, Key(), Loot(10), Enemy(10), Weapon(10), Potion(10))
    room4 = Room(3, 0, 0, None, Key(), Loot(10), Enemy(10), Weapon(10), Potion(10))
    room5 = Room(4, 0, 0, None, Key(), Loot(10), Enemy(10), Weapon(10), Potion(10))

    room_list = [room1, room2, room3, room4, room5]

    # Create a random graph
    G = nx.connected_watts_strogatz_graph(5, k=4, p=0.1)


    # Il mapping ha un problema, perché non tiene conto dei valori di default di x e y
    # Replace each node with a Room object
    mapping = {node : room_list[node] for node in G.nodes}
    G = nx.relabel_nodes(G, mapping)

    # Compute the positions of the nodes using the spring layout
    pos = nx.spring_layout(G)

    # Scale the positions to the size of the screen
    for node in pos:
        pos[node] = (pos[node][0] * WIDTH, pos[node][1] * HEIGHT)

    # Assign the positions to the rooms
    for room in G.nodes:
        x, y = pos[room]
        room.x = x * 144
        room.y = y * 112

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))  # Fill the screen with white
        # room.render_room(screen)
        for room in G.nodes:
            room.render_room(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()