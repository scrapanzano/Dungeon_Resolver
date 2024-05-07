"""
This module manages the project dungeon_gui
"""

from unified_planning.shortcuts import *
from termcolor import colored

import pygame
import sys

from dungeon_gui.Player import Player
from dungeon_gui.Weapon import Weapon
from dungeon_gui.hud import HUD
from dungeon_gui.Room import Room

from dungeon_gui.constants import PLAYER_GET_DAMAGE, PLAYER_GET_HEAL, PLAYER_ENTER_STARTING_POS,PLAYER_ENTER_ENDING_POS, WEAPON_ENTER_STARTING_POS, WEAPON_ENTER_ENDING_POS, PLAYER_EXIT_ENDING_POS, WEAPON_EXIT_ENDING_POS
from unified_planning.shortcuts import *

import re

#Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1270, 720

soundtrack = pygame.mixer.Sound("dungeon_resolver/sound_effects/soundtrack.wav")
soundtrack.set_volume(0.08)
escape_sound = pygame.mixer.Sound("dungeon_resolver/sound_effects/escape.wav")
escape_sound.set_volume(0.2)
door_open_sound = pygame.mixer.Sound("dungeon_resolver/sound_effects/door_open.wav")
door_open_sound.set_volume(0.4)
chest_open_sound = pygame.mixer.Sound("dungeon_resolver/sound_effects/chest_open.wav")
chest_open_sound.set_volume(0.4)
enemy_death_sound = pygame.mixer.Sound("dungeon_resolver/sound_effects/enemy_death.wav")
enemy_death_sound.set_volume(0.4)
out_transition_sound = pygame.mixer.Sound("dungeon_resolver/sound_effects/out_transition.wav")
out_transition_sound.set_volume(0.1)
in_transition_sound = pygame.mixer.Sound("dungeon_resolver/sound_effects/in_transition.wav")
in_transition_sound.set_volume(0.1)
collect_sword_sound = pygame.mixer.Sound("dungeon_resolver/sound_effects/collect_sword.wav")
collect_sword_sound.set_volume(0.4)
drink_potion_sound = pygame.mixer.Sound("dungeon_resolver/sound_effects/drink_potion.wav")
drink_potion_sound.set_volume(0.4)
collect_key_sound = pygame.mixer.Sound("dungeon_resolver/sound_effects/collect_key.wav")
collect_key_sound.set_volume(0.4)
collect_potion_sound = pygame.mixer.Sound("dungeon_resolver/sound_effects/collect_potion.wav")
collect_potion_sound.set_volume(0.4)



class GUI():
    """
    This class manages the project GUI
    """
    def __init__(self, problem, result, rooms):
        #Initialize pygame
        pygame.init()
        self.problem = problem
        self.result = result
        self.rooms = rooms


    def run(self):
        """
        Run the GUI
        """
        # Play the soundtrack
        soundtrack.play(-1)
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
        defeated_enemy_counter = FluentExp(self.problem.fluent("defeated_enemy_counter"))

        # Extract the goals
        goals = str(self.problem.goals)
        # Using re.findall() to find all sequences of digits in the string
        goals_values_str = re.findall(r'\d+', goals)
        # Converts the goals_value to a list of integers
        goals_values = list(map(int, goals_values_str))

        # Extract the goals
        hero_loot_goal = goals_values[0]
        hero_life_goal = goals_values[1]
        defeated_enemy_counter_goal = goals_values[2]


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
        player = Player(current_health=initial_hero_life, max_health=initial_max_hero_life, weapon=Weapon(damage=initial_weapon_damage))

        # Set up the HUD attributes based on the initial state
        initial_hero_loot = fluent_to_int(state, hero_loot)
        initial_key_counter = fluent_to_int(state, key_counter)
        initial_potion_counter = fluent_to_int(state, potion_counter)
        initial_defeated_enemy_counter = fluent_to_int(state, defeated_enemy_counter)

        # Get the escape room
        for room in self.rooms:
            if room.is_exit:
                escape_room_id = room.id

        # Create a HUD object
        hud = HUD(escape_room=escape_room_id, hero_loot=initial_hero_loot, hero_loot_goal=hero_loot_goal, key_counter=initial_key_counter, potion_counter=initial_potion_counter,room_id=actual_room.id, defeated_enemy_counter=initial_defeated_enemy_counter, defeated_enemy_counter_goal=defeated_enemy_counter_goal)

        # Set up the clock
        clock = pygame.time.Clock()

        # Set up the action name, usefull for displaying the last action on the screen
        action = ""

        # Flag to check if the player has entered the dungeon for the first time
        entered = False

        # Set up the transition room
        transition_room = Room(id="", has_door=True)

    
        # Game loop

        while True and not simulator.is_goal(state):
            clock.tick(60)
            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                    return
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
                        
                        if not last_action_name == "open_door":
                            # Get the old room id
                            old_room_id = room1[1]
                            # If the room id has more than 2 characters, then the room id is a double digit number
                            if len(room1) > 2:
                                old_room_id += room1[2]
                        else:
                            # If the last action was open_door, then the old room id is the transition room id
                            old_room_id = transition_room.id

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
                        collect_sword_sound.play()
                        last_action_name = "collect_weapon"

                    elif action.startswith("collect_treasure"):
                        actual_room.collect_treasure()
                        chest_open_sound.play()
                        last_action_name = "collect_treasure"
                
                    elif action.startswith("collect_key"):
                        actual_room.collect_key()
                        collect_key_sound.play()
                        last_action_name = "collect_key"
                
                    elif action.startswith("collect_potion"):
                        player.collect_potion(actual_room.potion)
                        actual_room.collect_potion()
                        collect_potion_sound.play()
                        last_action_name = "collect_potion"

                    elif action.startswith("defeat_enemy"):
                        actual_room.defeat_enemy()
                        enemy_death_sound.play()
                        player.get_damage(actual_room.enemy.damage)
                        last_action_name = "defeat_enemy"

                    elif action.startswith("drink_potion"):
                        player.get_heal()
                        drink_potion_sound.play()
                        last_action_name = "drink_potion"
            
                    elif action.startswith("open_door"):
                        temp_room = actual_room
                        # Exit room animation
                        exit_room(player, screen, actual_room, hud)
                        # Entering in the transition room
                        enter_room(player, screen, transition_room, hud)
                        update_hud(hud, state, hero_loot, key_counter, potion_counter,transition_room.id, action, defeated_enemy_counter)
                        
                        hud.render(screen)
                        pygame.display.flip()

                        actual_room = transition_room

                        screen.fill((37, 19, 26))
                        actual_room.render(screen)
                        player.render_player(screen, actual_room.scale_factor)
                        player.weapon.render_collectable(screen, actual_room.scale_factor - 1)
                        hud.render(screen)
                        pygame.display.flip()
                        
                        pygame.time.wait(1000)
                        # Set the transition room has_door attribute to False
                        transition_room.has_door = False
                        actual_room = transition_room
                        
                        screen.fill((37, 19, 26))  
                        actual_room.render(screen)
                        player.render_player(screen, actual_room.scale_factor)
                        player.weapon.render_collectable(screen, actual_room.scale_factor - 1)
                        hud.render(screen)

                        door_open_sound.play()
                        pygame.display.flip()
                        last_action_name = "open_door"
                        pygame.time.wait(1000)

                        ai = self.result.plan.actions[action_number + 1]
                        action = str(ai)

                        if not action.startswith("move"):
                            exit_room(player, screen, actual_room, hud)
                            enter_room(player, screen, temp_room, hud)
                            actual_room = temp_room
                            update_hud(hud, state, hero_loot, key_counter, potion_counter,actual_room.id, action, defeated_enemy_counter)
                           
                            hud.render(screen)
                            pygame.display.flip()

                    elif action.startswith("escape_from_dungeon"):
                        exit_room(player, screen, actual_room, hud)
                        last_action_name = "escape_from_dungeon"
                
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
                update_hud(hud, state, hero_loot, key_counter, potion_counter,old_room_id, action, defeated_enemy_counter, old_room.is_exit)
                exit_room(player, screen, old_room, hud)
                if not transition_room.has_door:
                    transition_room.has_door = True
                pygame.time.wait(500)
                update_hud(hud, state, hero_loot, key_counter, potion_counter,new_room_id, action, defeated_enemy_counter, actual_room.is_exit)
                enter_room(player, screen, actual_room, hud)
                pygame.time.wait(1000)
                last_action_name = ""

            update_hud(hud, state, hero_loot, key_counter, potion_counter,actual_room.id, action, defeated_enemy_counter, actual_room.is_exit)
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

        soundtrack.stop()
        escape_sound.play()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                    return
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

def exit_room(player, screen, room, hud):
    """
    Updates room rendering when player leaves room

    Parameters
    ----------
    :param player: Player object
    :type player: Player 
    :param screen: Screen where dungeon_gui runs
    :type screen: pygame Surface
    :param room: Room the player is exiting
    :type room: Room 
    :param hud: HUD object
    :type hud: HUD 
    """
    out_transition_sound.play()
    player_target_y = PLAYER_EXIT_ENDING_POS[1]
    weapon_target_y = WEAPON_EXIT_ENDING_POS[1]
    player.is_moving = True
    while player.is_moving:
        screen.fill((37, 19, 26))
        room.render(screen)
        hud.render(screen)
        player.player_pos_y = pygame.math.lerp(player.player_pos_y, player_target_y, 0.01)
        player.weapon.pos_y = pygame.math.lerp(player.weapon.pos_y, weapon_target_y, 0.01)

        if abs(player.weapon.pos_y - weapon_target_y) < 0.01:
            player.weapon.pos_y = weapon_target_y

        if abs(player.player_pos_y - player_target_y) < 0.01:
            player.player_pos_y = player_target_y
            player.is_moving = False
        player.render_player(screen, room.scale_factor)  
        player.weapon.render_collectable(screen, room.scale_factor - 1)
        pygame.display.flip()


def enter_room(player, screen, room, hud):
    """
    Updates room rendering when player enters the room

    Parameters  
    ----------
    :param player: Player object
    :type player: Player 
    :param screen: Screen where dungeon_gui runs
    :type screen: pygame Surface
    :param room: Room the player is entering
    :type room: Room 
    :param hud: HUD object
    :type hud: HUD 
    """
    in_transition_sound.play()
    player.player_pos_y = PLAYER_ENTER_STARTING_POS[1]
    player.weapon.pos_y = WEAPON_ENTER_STARTING_POS[1]
    player_target_y = PLAYER_ENTER_ENDING_POS[1]
    weapon_target_y = WEAPON_ENTER_ENDING_POS[1]
    player.is_moving = True
    while player.is_moving:
        screen.fill((37, 19, 26))
        room.render(screen)
        hud.render(screen)
        player.player_pos_y = pygame.math.lerp(player.player_pos_y, player_target_y, 0.01)
        player.weapon.pos_y = pygame.math.lerp(player.weapon.pos_y, weapon_target_y, 0.01)
        
        if abs(player.weapon.pos_y - weapon_target_y) < 0.01:
            player.weapon.pos_y = weapon_target_y

        if abs(player.player_pos_y - player_target_y) < 0.01:
            player.player_pos_y = player_target_y
            player.is_moving = False
        player.render_player(screen, room.scale_factor)
        player.weapon.render_collectable(screen, room.scale_factor - 1)
        pygame.display.flip()


def fluent_to_int(state, fluent):
    """
    Converts unified_planning Fluent to int

    Parameters
    ----------
    :param state: Object representing the state of the problem
    :type state: unified_planning.shortcuts.State
    :param fluent: Object representing a fluent
    :type fluent: unified_planning.shortcuts.FluentExp
    
    Returns
    -------
    :returns: The value of the fluent as an integer
    :rtype: int

    """
    return int(str(state.get_value(fluent)))


def update_hud(hud, state, hero_loot, key_counter, potion_counter, actual_room_id, action, defeated_enemy_counter=None, is_exit=False):
    
    """
    Updates all hud variables

    Parameters
    ----------
    :param hud: HUD object
    :type hud: HUD 
    :param state: Object representing the state of the problem
    :type state: unified_planning.shortcuts.State
    :param hero_loot: Object representing the hero loot fluent
    :type hero_loot: unified_planning.shortcuts.FluentExp
    :param key_counter: Object representing the key counter fluent
    :type key_counter: unified_planning.shortcuts.FluentExp
    :param potion_counter: Object representing the potion counter fluent
    :type potion_counter: unified_planning.shortcuts.FluentExp
    :param actual_room_id: The id of the actual room
    :type actual_room_id: int
    :param action: The last action executed
    :type action: str
    :param defeated_enemy_counter: Object representing the defeated enemy counter fluent
    :type defeated_enemy_counter: unified_planning.shortcuts.FluentExp
    :param is_exit: Flag to check if the actual room is the exit room
    :type is_exit: bool

    """
    
    hud.update_hero_loot(fluent_to_int(state, hero_loot))
    hud.update_keys(state.get_value(key_counter))
    hud.update_potions(state.get_value(potion_counter))
    hud.update_id(actual_room_id, is_exit)
    hud.update_action(action)
    if defeated_enemy_counter is not None:
        hud.update_defeated_enemy_counter(fluent_to_int(state, defeated_enemy_counter))

