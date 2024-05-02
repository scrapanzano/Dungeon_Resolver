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

from classes.constants import PLAYER_GET_DAMAGE, PLAYER_GET_HEAL, PLAYER_ENTER_STARTING_POS,PLAYER_ENTER_ENDING_POS, WEAPON_ENTER_ENDING_POS, PLAYER_EXIT_ENDING_POS, WEAPON_EXIT_ENDING_POS
from unified_planning.shortcuts import *
from unified_planning.io import PDDLReader

import networkx as nx

from classes.constants import PLAYER_GET_DAMAGE, PLAYER_GET_HEAL


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
    room2 = Room(id = 2, key=None, loot=Loot(40), enemy=None, weapon=Weapon(damage=50, weapon_pos_x=6.1, weapon_pos_y=7.6), potion=None, has_door=False)
    room3 = Room(id = 3, key=None, loot=None, enemy=Enemy(50), weapon=None, potion=None, has_door=False)
    room4 = Room(id = 4, key=None, loot=Loot(40), enemy=None, weapon=None, potion=Potion(10), has_door=False)
    room5 = Room(id = 5, key=None, loot=Loot(30), enemy=None, weapon=Weapon(50, weapon_pos_x=6.1, weapon_pos_y=7.6), potion=Potion(30), has_door=False)
    room6 = Room(id = 6, key=None, loot=None, enemy=Enemy(70), weapon=None, potion=Potion(50), has_door=False)
    room7 = Room(id = 7, key=None, loot=None, enemy=None, weapon=Weapon(70, weapon_pos_x=6.1, weapon_pos_y=7.6), potion=None, has_door=False)

    rooms = [room0, room1, room2, room3, room4, room5, room6, room7]

    actual_room = rooms[0]

    actual_room.x = (WIDTH  - actual_room.width) // 2
    actual_room.y = (HEIGHT - actual_room.height) // 2

    # Using unified-planning for reading the domain and instance files
    reader = PDDLReader()
    problem = reader.parse_problem("./dungeon_resolver/dungeon_domain.pddl", "./dungeon_resolver/dungeon_problem.pddl")
    
    # Invoke unified-planning planner enhsp
    up.shortcuts.get_environment().credits_stream = None # Disable printing of planning engine credits
    

    with OneshotPlanner(name='enhsp') as planner:
        result = planner.solve(problem)
        print("%s returned: %s\n" % (planner.name, result.plan))

    # Invoke unified-planning sequential simulator
    hero_life = FluentExp(problem.fluent("hero_life"))
    max_hero_life = FluentExp(problem.fluent("max_hero_life"))
    hero_strength = FluentExp(problem.fluent("hero_strength"))
    hero_loot = FluentExp(problem.fluent("hero_loot"))
    key_counter = FluentExp(problem.fluent("key_counter"))
    potion_counter = FluentExp(problem.fluent("potion_counter"))

    simulator = SequentialSimulator(problem)

    state = simulator.get_initial_state()

    action_number = 0
    last_action_time = pygame.time.get_ticks()
    last_action_name = ""

    initial_hero_life = fluent_to_int(state, hero_life)
    initial_max_hero_life = fluent_to_int(state, max_hero_life)
    initial_weapon_damage = fluent_to_int(state, hero_strength)

    player = Player(current_health=initial_hero_life, max_health=initial_max_hero_life, weapon=Weapon(damage=initial_weapon_damage + 30))

    initial_hero_loot = fluent_to_int(state, hero_loot)
    initial_key_counter = fluent_to_int(state, key_counter)
    initial_potion_counter = fluent_to_int(state, potion_counter)

    hud = HUD(hero_loot=initial_hero_loot, key_counter=initial_key_counter, potion_counter=initial_potion_counter,room_id=actual_room.id)

    clock = pygame.time.Clock()

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

        current_time = pygame.time.get_ticks()

        if current_time - last_action_time >= 2000 and not player.is_moving:  # 2000 milliseconds = 2 seconds
            if action_number < len(result.plan.actions):
                ai = result.plan.actions[action_number]
                state = simulator.apply(state, ai)
                action = str(ai)

                if action.startswith("move"):
                    # Remove 'move(' from the start and ')' from the end
                    args_str = action[len('move('):-1]
                    # Split the remaining string into weapon and room
                    room1, room2 = args_str.split(', ')
                    new_room_id = room2[1]
                    #Hanno delle posizioni diverse
                    old_room = actual_room
                    actual_room = rooms[int(new_room_id)]
                    last_action_name = "move"

                elif action.startswith("collect_weapon"):
                    player.update_weapon(actual_room.weapon.damage)
                    actual_room.collect_weapon()
                    last_action_name = "collect_weapon"

                elif action.startswith("collect_treasure"):
                    actual_room.collect_treasure()
                    last_action_name = "collect_treasure"
                
                elif action.startswith("collect_key"):
                    actual_room.collect_key()
                    last_action_name = "collect_key"
                
                elif action.startswith("collect_potion"):
                    actual_room.collect_potion()
                    last_action_name = "collect_potion"

                elif action.startswith("defeat_enemy"):
                    actual_room.defeat_enemy()
                    player.get_damage(actual_room.enemy.damage)
                    last_action_name = "defeat_enemy"

                elif action.startswith("drink_potion"):
                    player.get_heal(actual_room.potion.potion_value)
                    last_action_name = "drink_potion"
            
                elif action.startswith("open_door"):
                    last_action_name = "open_door"
                    pass

                elif action.startswith("escape_from_dungeon"):
                    last_action_name = "escape_from_dungeon"
                    pass

            action_number += 1
            last_action_time = current_time


        if last_action_name == "move":
            print("Starting movement")
            target_y = PLAYER_EXIT_ENDING_POS[1]
            player.is_moving = True
            while player.is_moving:
                screen.fill((37, 19, 26))
                old_room.render(screen)
                hud.render(screen)
                player.player_pos_y = pygame.math.lerp(player.player_pos_y, target_y, 0.05)
                if abs(player.player_pos_y - target_y) < 0.01:
                    player.player_pos_y = target_y
                    player.is_moving = False
                player.render_player(screen, actual_room.x, actual_room.y, actual_room.scale_factor)  
                pygame.display.flip()
            player.player_pos_y = PLAYER_ENTER_STARTING_POS[1]
            target_y = PLAYER_ENTER_ENDING_POS[1]
            player.is_moving = True
            while player.is_moving:
                screen.fill((37, 19, 26))
                actual_room.render(screen)
                hud.render(screen)
                player.player_pos_y = pygame.math.lerp(player.player_pos_y, target_y, 0.05)
                if abs(player.player_pos_y - target_y) < 0.01:
                    player.player_pos_y = target_y
                    player.is_moving = False
                player.render_player(screen, actual_room.x, actual_room.y, actual_room.scale_factor)
                pygame.display.flip()
            last_action_name = ""
            print("Ending movement")
    
        update_hud(hud, state, hero_loot, key_counter, potion_counter,actual_room.id)
        screen.fill((37, 19, 26))  
        actual_room.render(screen)
        player.render_player(screen, actual_room.x, actual_room.y, actual_room.scale_factor)
        player.weapon.render_collectable(screen, actual_room.scale_factor - 1)
        hud.render(screen)

        pygame.display.flip()

def fluent_to_int(state, fluent):
    return int(str(state.get_value(fluent)))

def update_hud(hud, state, hero_loot, key_counter, potion_counter,actual_room_id):
    hud.update_hero_loot(state.get_value(hero_loot))
    hud.update_keys(state.get_value(key_counter))
    hud.update_potions(state.get_value(potion_counter))
    hud.update_id(actual_room_id)

        
if __name__ == "__main__":
    Main()