import pygame
import sys
import time

from classes.Player import Player
from classes.Room import Room
from classes.Weapon import Weapon
from classes.Key import Key
from classes.Loot import Loot
from classes.Enemy import Enemy
from classes.Potion import Potion
from classes.hud import HUD
from classes.constants import PLAYER_GET_DAMAGE, PLAYER_GET_HEAL

from unified_planning.shortcuts import *
from unified_planning.io import PDDLReader

import networkx as nx

# Initialize pygame
pygame.init()


# Set up the display
WIDTH, HEIGHT = 1270, 720


# Main loop
def Main():

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dungeon")


    G = nx.Graph()

    room0 = Room(id = 0, key=None, loot=None, enemy=None, weapon=None, potion=None, has_door=False)
    room1 = Room(id = 1, key=None, loot=None, enemy=Enemy(50), weapon=None, potion=None, has_door=False)
    room2 = Room(id = 2, key=None, loot=Loot(40), enemy=None, weapon=Weapon(50), potion=None, has_door=False)
    room3 = Room(id = 3, key=None, loot=None, enemy=Enemy(50), weapon=None, potion=None, has_door=False)
    room4 = Room(id = 4, key=None, loot=Loot(40), enemy=None, weapon=None, potion=Potion(10), has_door=False)
    room5 = Room(id = 5, key=None, loot=Loot(30), enemy=None, weapon=Weapon(50), potion=Potion(30), has_door=False)
    room6 = Room(id = 6, key=None, loot=None, enemy=Enemy(70), weapon=None, potion=Potion(50), has_door=False)
    room7 = Room(id = 7, key=None, loot=None, enemy=None, weapon=Weapon(70), potion=None, has_door=False)

    rooms = [room0, room1, room2, room3, room4, room5, room6, room7]

    # player_weapon = Weapon(damage=40, weapon_pos_x=6.8, weapon_pos_y=10)
    player = Player(max_health=100, weapon=Weapon())

    actual_room = rooms[3]

    actual_room.x = (WIDTH  - actual_room.width) // 2
    actual_room.y = (HEIGHT - actual_room.height) // 2

    hud = HUD(id=actual_room.id)

    # Using unified-planning for reading the domain and instance files
    reader = PDDLReader()
    problem = reader.parse_problem("./dungeon_resolver/dungeon_domain.pddl", "./dungeon_resolver/dungeon_problem.pddl")
    
    # Invoke unified-planning planner enhsp
    up.shortcuts.get_environment().credits_stream = None # Disable printing of planning engine credits
    

    with OneshotPlanner(name='enhsp') as planner:
        result = planner.solve(problem)
        print("%s returned: %s\n" % (planner.name, result.plan))

    # Invoke unified-planning sequential simulator
    #life = FluentExp(problem.fluent("hero_life"))
    #strength = FluentExp(problem.fluent("hero_strength"))
    loot = FluentExp(problem.fluent("hero_loot"))

    keys = FluentExp(problem.fluent("key_counter"))

    simulator = SequentialSimulator(problem)

    travel = False

    damaged = False
    healed = False

    clock = pygame.time.Clock()

    state = simulator.get_initial_state()

    action_number = 0

    last_action_time = pygame.time.get_ticks()

    while True and not simulator.is_goal(state):
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

        current_time = pygame.time.get_ticks()
        if current_time - last_action_time >= 2000:  # 2000 milliseconds = 2 seconds
            if action_number < len(result.plan.actions):
                ai = result.plan.actions[action_number]
                state = simulator.apply(state, ai)
                hud.update_hero_loot(state.get_value(loot))
                hud.update_keys(state.get_value(keys))
                hud.update_id(actual_room.id)
                action_number += 1
            last_action_time = current_time

         

        pygame.display.flip()

        
        
if __name__ == "__main__":
    Main()