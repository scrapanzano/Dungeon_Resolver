"""
This module manages the project dungeon_gui
"""

from unified_planning.shortcuts import *
from termcolor import colored

import pygame
import sys
import time

from dungeon_gui.Player import Player
from dungeon_gui.Room import Room
from dungeon_gui.Weapon import Weapon
from dungeon_gui.Key import Key
from dungeon_gui.Loot import Loot
from dungeon_gui.Enemy import Enemy
from dungeon_gui.Potion import Potion
from dungeon_gui.hud import HUD

from dungeon_gui.constants import PLAYER_GET_DAMAGE, PLAYER_GET_HEAL, PLAYER_ENTER_STARTING_POS,PLAYER_ENTER_ENDING_POS, WEAPON_ENTER_STARTING_POS, WEAPON_ENTER_ENDING_POS, PLAYER_EXIT_ENDING_POS, WEAPON_EXIT_ENDING_POS
from unified_planning.shortcuts import *
from unified_planning.io import PDDLReader

import networkx as nx

import ctypes


# Set up the display
WIDTH, HEIGHT = 1270, 720


class GUI():
    """
    This class manages the project GUI
    """
    def __init__(self, problem, result, rooms):
        self.problem = problem
        self.result = result
        self.rooms = rooms

        #Initialize pygame
        pygame.init()


    def run(self):
        """
        TODO: add docs
        """
        # Set up the display
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # Set up the displayed name
        pygame.display.set_caption("Dungeon")

        # Set up the first room
        actual_room = self.rooms[0]

        # Set up the rooom in the middle of the screen
        actual_room.x = (WIDTH  - actual_room.width) // 2
        actual_room.y = (HEIGHT - actual_room.height) // 2

        # Invoke unified-planning planner enhsp

        # Disable printing of planning engine credits
        up.shortcuts.get_environment().credits_stream = None 

        # Creating fluent expressions
        hero_life = FluentExp(self.problem.fluent("hero_life"))
        max_hero_life = FluentExp(self.problem.fluent("max_hero_life"))
        hero_strength = FluentExp(self.problem.fluent("hero_strength"))
        hero_loot = FluentExp(self.problem.fluent("hero_loot"))
        key_counter = FluentExp(self.problem.fluent("key_counter"))
        potion_counter = FluentExp(self.problem.fluent("potion_counter"))

        # Invoke unified-planning sequential simulator
        simulator = SequentialSimulator(self.problem)

        # Get initial state
        state = simulator.get_initial_state()

        # Set up the action counter
        action_number = 0
        # Set up the last action time
        last_action_time = pygame.time.get_ticks()
        # Set up the last action name
        last_action_name = ""

        # Set up player attributes based on the initial state
        initial_hero_life = fluent_to_int(state, hero_life)
        initial_max_hero_life = fluent_to_int(state, max_hero_life)
        initial_weapon_damage = fluent_to_int(state, hero_strength)

        # Create a player object
        player = Player(current_health=initial_hero_life, max_health=initial_max_hero_life, weapon=Weapon(damage=initial_weapon_damage + 30))

        # Set up the HUD attributes based on the initial state
        initial_hero_loot = fluent_to_int(state, hero_loot)
        initial_key_counter = fluent_to_int(state, key_counter)
        initial_potion_counter = fluent_to_int(state, potion_counter)

        # Create a HUD object
        hud = HUD(hero_loot=initial_hero_loot, key_counter=initial_key_counter, potion_counter=initial_potion_counter,room_id=actual_room.id)

        # Set up the clock
        clock = pygame.time.Clock()

        # Set up the action name, usefull for displaying the last action on the screen
        action = ""

        # Game loop

        entered = False

        while True and not simulator.is_goal(state):
            clock.tick(60)
            # Check for events
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

            # Getting the current time
            current_time = pygame.time.get_ticks()  

            # If at least 2 seconds have passed since the last action and the player is not moving
            # then the next action can be executed
            if current_time - last_action_time >= 2000 and not player.is_moving:  # 2000 milliseconds = 2 seconds
                if action_number < len(self.result.plan.actions):
                    ai = self.result.plan.actions[action_number]
                    state = simulator.apply(state, ai)
                    action = str(ai)

                    if action.startswith("move"):
                        # Remove 'move(' from the start and ')' from the end
                        args_str = action[len('move('):-1]
                        # Split the remaining string into weapon and room
                        room1, room2 = args_str.split(', ')
                        
                        # Get the old room id
                        old_room_id = room1[1]
                        # If the room id has more than 2 characters, then the room id is a double digit number
                        if len(room1) > 2:
                            old_room_id += room1[2]

                        # Get the new room id
                        new_room_id = room2[1]
                        # If the room id has more than 2 characters, then the room id is a double digit number
                        if len(room2) > 2:
                            new_room_id += room2[2]

                        old_room = actual_room
                        actual_room = self.rooms[int(new_room_id)]
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
                        player.collect_potion(actual_room.potion)
                        actual_room.collect_potion()
                        last_action_name = "collect_potion"

                    elif action.startswith("defeat_enemy"):
                        actual_room.defeat_enemy()
                        player.get_damage(actual_room.enemy.damage)
                        last_action_name = "defeat_enemy"

                    elif action.startswith("drink_potion"):
                        player.get_heal()
                        last_action_name = "drink_potion"
            
                    elif action.startswith("open_door"):
                        last_action_name = "open_door"
                        pass

                    elif action.startswith("escape_from_dungeon"):
                        last_action_name = "escape_from_dungeon"
                        exit_room(player, screen, old_room, hud)
                
                # Update the action number and the last action time
                action_number += 1
                last_action_time = current_time
            
            # First entrance in the room
            if action_number == 0 and not entered:
                entered = True
                enter_room(player, screen, actual_room, hud)
                pygame.time.wait(500)

            # If the last action was a move action, the player has to exit the room
            # and then enter the new room
            if last_action_name == "move":
                update_hud(hud, state, hero_loot, key_counter, potion_counter,old_room_id, action)
                exit_room(player, screen, old_room, hud)
                pygame.time.wait(500)
                update_hud(hud, state, hero_loot, key_counter, potion_counter,new_room_id, action)
                enter_room(player, screen, actual_room, hud)
                pygame.time.wait(1000)
                last_action_name = ""

            update_hud(hud, state, hero_loot, key_counter, potion_counter,actual_room.id, action)
            screen.fill((37, 19, 26))  
            actual_room.render(screen)
            player.render_player(screen, actual_room.scale_factor)
            player.weapon.render_collectable(screen, actual_room.scale_factor - 1)
            hud.render(screen)

            pygame.display.flip()

        # Load the font for the text
        big_font = pygame.font.Font("dungeon_Resolver/dungeon_gui/fonts/Minecraft.ttf", 100)
        # Create the text surface
        big_text = big_font.render("Mission Complete", True, (255, 255, 255))
        # Create a rect for the text surface
        big_text_rect = big_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        # Load the font for the text
        small_font = pygame.font.Font("dungeon_Resolver/dungeon_gui/fonts/Minecraft.ttf", 30)
        # Create the text surface
        small_text = small_font.render("press q or top right cross to quit", True, (255, 255, 255))
        # Create a rect for the text surface
        small_text_rect = small_text.get_rect(center=(WIDTH // 2, (HEIGHT // 2) + small_text.get_height() * 2))


        # Create a semi-transparent surface
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 128))  # RGBA color, the last value is the alpha (transparency)

        while True:
            # Redraw the screen to be visible behind the semi-transparent surface
            screen.fill((37, 19, 26))  
            actual_room.render(screen)
            hud.render(screen)
            player.render_player(screen, actual_room.scale_factor)
            # Draw the semi-transparent surface and the text on the screen
            screen.blit(overlay, (0, 0))
            # Draw the text on the screen
            screen.blit(big_text, big_text_rect)
            screen.blit(small_text, small_text_rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                    sys.exit()


def exit_room(player, screen, old_room, hud):
    """
    TODO: add docs

    Parameters
    ----------
    :param screen: Screen where dungeon_gui runs
    :type screen: pygame Surface
    :param old_room: TODO
    :type old_room: TODO
    :param hud: TODO
    :type hud: TODO
    """
    player_target_y = PLAYER_EXIT_ENDING_POS[1]
    weapon_target_y = WEAPON_EXIT_ENDING_POS[1]
    player.is_moving = True
    while player.is_moving:
        screen.fill((37, 19, 26))
        old_room.render(screen)
        hud.render(screen)
        player.player_pos_y = pygame.math.lerp(player.player_pos_y, player_target_y, 0.01)
        player.weapon.pos_y = pygame.math.lerp(player.weapon.pos_y, weapon_target_y, 0.01)

        if abs(player.weapon.pos_y - weapon_target_y) < 0.01:
            player.weapon.pos_y = weapon_target_y

        if abs(player.player_pos_y - player_target_y) < 0.01:
            player.player_pos_y = player_target_y
            player.is_moving = False
        player.render_player(screen, old_room.scale_factor)  
        player.weapon.render_collectable(screen, old_room.scale_factor - 1)
        pygame.display.flip()


def enter_room(player, screen, actual_room, hud):
    """
    TODO: add docs

    Parameters
    ----------
    :param screen: Screen where dungeon_gui runs
    :type screen: pygame Surface
    :param actual_room: TODO
    :type actual_room: TODO
    :param hud: TODO
    :type hud: TODO
    """
    player.player_pos_y = PLAYER_ENTER_STARTING_POS[1]
    player.weapon.pos_y = WEAPON_ENTER_STARTING_POS[1]
    player_target_y = PLAYER_ENTER_ENDING_POS[1]
    weapon_target_y = WEAPON_ENTER_ENDING_POS[1]
    player.is_moving = True
    while player.is_moving:
        screen.fill((37, 19, 26))
        actual_room.render(screen)
        hud.render(screen)
        player.player_pos_y = pygame.math.lerp(player.player_pos_y, player_target_y, 0.01)
        player.weapon.pos_y = pygame.math.lerp(player.weapon.pos_y, weapon_target_y, 0.01)
        
        if abs(player.weapon.pos_y - weapon_target_y) < 0.01:
            player.weapon.pos_y = weapon_target_y

        if abs(player.player_pos_y - player_target_y) < 0.01:
            player.player_pos_y = player_target_y
            player.is_moving = False
        player.render_player(screen, actual_room.scale_factor)
        player.weapon.render_collectable(screen, actual_room.scale_factor - 1)
        pygame.display.flip()


def fluent_to_int(state, fluent):
    """
    TODO: add docs

    Parameters
    ----------
    :param state: TODO
    :type state: TODO
    :param fluent: TODO
    :type fluent: TODO
    
    Returns
    -------
    :returns: TODO
    :rtype: int
    """
    return int(str(state.get_value(fluent)))


def update_hud(hud, state, hero_loot, key_counter, potion_counter, actual_room_id, action):
    """
    TODO: add docs

    Parameters
    ----------
    :param state: TODO
    :type state: TODO
    :param hero_loot: TODO
    :type hero_loot: int
    :param potion_counter: TODO
    :type potion_counter: int
    :param actual_room_id: TODO
    :type actual_room_id: TODO
    :param action: TODO
    :type action: TODO
    """
    hud.update_hero_loot(state.get_value(hero_loot))
    hud.update_keys(state.get_value(key_counter))
    hud.update_potions(state.get_value(potion_counter))
    hud.update_id(actual_room_id)
    hud.update_action(action)
