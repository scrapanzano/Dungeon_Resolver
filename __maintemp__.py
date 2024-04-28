import sys
import os
import argparse
import math
import random
import string
from string import Template
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.lines as lines
from unified_planning.shortcuts import *
from unified_planning.io import PDDLReader
from termcolor import colored

template_name = "./dungeon_resolver/dungeon_template.pddl"

'''
Generates dungeon instance
'''
def generate_instance(instance_name, num_rooms):
    with open( template_name ) as instream :
        text = instream.read()
        template = string.Template( text )
    
    # Generate a random dungeon in which each room is connected at least with another one
    G = nx.connected_watts_strogatz_graph(num_rooms, k=4, p=0.1)

    start_room = 0

    exit_room = farthest_node(G, start_room)

    generate_doors(G)

    # List of rooms in which there's a key 
    key_rooms = generate_keys(G, start_room, exit_room)

    # Dict of rooms in wich there's a treasure [format: {room : treasure_value}]
    treasure_probability = 0.4 # 40%
    num_treasure_rooms = (int)(num_rooms * treasure_probability) 
    treasure_rooms = generate_treasures(G, start_room, num_treasure_rooms)

    # Generating loot_goal
    loot_rate = 0.35 # 35%
    loot_goal = generate_loot_goal(treasure_rooms, loot_rate)

    # Dict of rooms in wich there's an enemy [format: {room : enemy_value(life/strength)}]
    enemy_probability = 0.40 # 40%
    num_enemy_rooms = (int)(num_rooms * enemy_probability)
    enemy_rooms = generate_enemies(G, start_room, num_enemy_rooms)

    defeated_enemy_goal = (int)(num_enemy_rooms * 0.2) # 20%

    # List of safe rooms (in which there's not an enemy)
    safe_rooms = []
    for node in G.nodes():
        if node not in list(enemy_rooms):
            safe_rooms.append(node)

    # Dict of rooms in wich there's a weapon [format: {room : weapon_strength}]
    weapon_rooms = generate_weapons(G, start_room, enemy_rooms)

    # Dict of rooms in wich there's a potion [format: {room : potion_value}]
    potion_probability = 0.4 # 40%
    num_potion_rooms = (int)(num_rooms * potion_probability)
    potion_rooms = generate_potions(G, start_room, num_potion_rooms)

    # List of safe rooms (no enemy) in which there's not a treasure, weapon or potion
    standard_rooms = []
    for node in G.nodes():
        if node not in list(treasure_rooms) + list(weapon_rooms) + list(potion_rooms) and node in safe_rooms:
            standard_rooms.append(node)

    # Creating the string that containts the room_list
    room_list = ''

    for i in range(num_rooms):
        room_list += 'R' + str(i) + ' '

    # Creating the string that contains the treasures_list
    treasures_list = ''

    for i in range(len(treasure_rooms)):
        treasures_list += 'T' + str(i) + ' '

    # Creating the string that contains the enemies_list
    enemies_list = ''

    for i in range(len(enemy_rooms)):
        enemies_list += 'E' + str(i) + ' '

    # Creating the string that contains the weapons_list
    weapons_list = ''

    for i in range(len(weapon_rooms)):
        weapons_list += 'W' + str(i) + ' '

    # Creating the string that contains the potions_list
    potions_list = ''

    for i in range(len(potion_rooms)):
        potions_list += 'P' + str(i) + ' '

    # Creating the string that describes how all the rooms are connected with each others
    room_links = ''

    for room in G.nodes:
        for neighbor in G.neighbors(room):
            if G[room][neighbor]['type'] == 'normal':
                room_links += '(connected R' + str(room) + ' R' + str(neighbor) + ') ' 

    closed_doors = ''

    for room in G.nodes:
        for neighbor in G.neighbors(room):
            if G[room][neighbor]['type'] == 'door':
                closed_doors += '(closed_door R' + str(room) + ' R' + str(neighbor) + ') '

    # Creating the string that containts the safe rooms
    safe_rooms_list = ''
    
    for room in safe_rooms:
        safe_rooms_list += '(room_safe R' +str(room) + ') '

    # Creating the string that containts the keys location
    keys_location = ''

    for key_room in key_rooms:
        keys_location += '(key_at R' + str(key_room) + ') '

    # Creating the string that containts the treasures location and value
    treasures_location = ''
    treasures_value = ''
    t_index = 0

    for room in treasure_rooms:
        treasure_name = 'T' + str(t_index)
        treasure_value = treasure_rooms[room]
        treasures_location += '(treasure_at ' + treasure_name + ' R' + str(room) + ') '
        treasures_value += '(= (treasure_value ' + treasure_name + ') ' + str(treasure_value) +') '
        t_index += 1

    # Creating the string that containts the enemies location, life and strength
    enemies_location = ''
    enemies_life = ''
    enemies_strength = ''
    e_index = 0

    for room in enemy_rooms:
        enemy_name = 'E' + str(e_index)
        enemy_value = enemy_rooms[room]
        enemies_location += '(enemy_at ' + enemy_name + ' R' + str(room) + ') '
        enemies_life += '(= (enemy_life ' + enemy_name + ') ' + str(enemy_value) +') '
        enemies_strength += '(= (enemy_strength ' + enemy_name + ') ' + str(enemy_value) +') '
        e_index += 1
    
    # Creating the string that containts the weapons location and strength
    weapons_location = ''
    weapons_strength = ''
    w_index = 0

    for room in weapon_rooms:
        weapon_name = 'W' + str(w_index)
        weapon_value = weapon_rooms[room]
        weapons_location += '(weapon_at ' + weapon_name + ' R' + str(room) + ') '
        weapons_strength += '(= (weapon_strength ' + weapon_name + ') ' + str(weapon_value) +') '
        w_index += 1

    # Creating the string that containts the potions location and value
    potions_location = ''
    potions_value = ''
    p_index = 0

    for room in potion_rooms:
        potion_name = 'P' + str(p_index)
        potion_value = potion_rooms[room]
        potions_location += '(potion_at ' + potion_name + ' R' + str(room) + ') '
        potions_value += '(= (potion_value ' + potion_name + ') ' + str(potion_value) +') '
        p_index += 1

    # Populate template
    template_mapping = dict()
    template_mapping['instance_name'] = instance_name
    template_mapping['domain_name'] = 'dungeon' 
    # Objects
    template_mapping['room_list'] = room_list
    template_mapping['treasures_list'] = treasures_list
    template_mapping['enemies_list'] = enemies_list
    template_mapping['weapons_list'] = weapons_list
    template_mapping['potions_list'] = potions_list
    # Init
    template_mapping['start_room'] = '(at R' + str(start_room) + ')'
    template_mapping['exit_room'] = '(exit_room R' + str(exit_room) + ')'
    template_mapping['room_links'] = room_links
    template_mapping['safe_rooms'] = safe_rooms_list
    template_mapping['closed_doors'] = closed_doors
    template_mapping['keys_location'] = keys_location
    template_mapping['key_counter'] = '(= (key_counter) 0)'
    template_mapping['treasures_location'] = treasures_location
    template_mapping['treasures_value'] = treasures_value
    template_mapping['enemies_location'] = enemies_location
    template_mapping['enemies_life'] = enemies_life
    template_mapping['enemies_strength'] = enemies_strength
    template_mapping['weapons_location'] = weapons_location
    template_mapping['weapons_strength'] = weapons_strength
    template_mapping['potions_location'] = potions_location
    template_mapping['potions_value'] = potions_value
    template_mapping['hero_life'] = '(= (hero_life) 100)'
    template_mapping['max_hero_life'] = '(= (max_hero_life) 100)'
    template_mapping['hero_strength'] = '(= (hero_strength) 0)'
    template_mapping['hero_loot'] = '(= (hero_loot) 0)'
    template_mapping['defeated_enemy_counter'] = '(= (defeated_enemy_counter) 0)'
    #Goal
    template_mapping['loot_goal'] = '(>= (hero_loot) ' + str(loot_goal) + ')' 
    template_mapping['life_goal'] = '(> (hero_life) 0)'
    template_mapping['defeated_enemy_goal'] = '(>= (defeated_enemy_counter) ' + str(defeated_enemy_goal) + ')'

    # Write file
    f = open('./dungeon_resolver/dungeon_problem.pddl', 'w')
    f.write(str(template.substitute(template_mapping)))
    f.close()

    # os.system("java -jar Dungeon_Resolver/enhsp.jar -o dungeon_resolver/simple_dungeon_domain.pddl -f dungeon_resolver/simple_dungeon_problem.pddl -planner opt-hrmax")

    # Using unified-planning for reading the domain and instance files
    reader = PDDLReader()
    problem = reader.parse_problem("./dungeon_resolver/dungeon_domain.pddl", "./dungeon_resolver/dungeon_problem.pddl")
    
    # Invoke unified-planning planner enhsp
    up.shortcuts.get_environment().credits_stream = None # Disable printing of planning engine credits
    
    choice = yes_or_no('Do you want enhsp optimal version?')
    print()
    if choice:
        selected_planner = 'enhsp-opt'
    else:
        selected_planner = 'enhsp'

    with OneshotPlanner(name=selected_planner) as planner:
        result = planner.solve(problem)
        print("%s returned: %s\n" % (planner.name, result.plan))

    # Invoke unified-planning sequential simulator
    life = FluentExp(problem.fluent("hero_life"))
    strength = FluentExp(problem.fluent("hero_strength"))
    loot = FluentExp(problem.fluent("hero_loot"))
    n_action = 1

    txt = open('./dungeon_resolver/sequential_simulator.txt', 'w') # Open file where save SequentialSimulator

    with SequentialSimulator(problem) as simulator: 
        state = simulator.get_initial_state()
        print(colored(f"Initial life = {state.get_value(life)}", 'green'))
        txt.write(f"Initial life = {state.get_value(life)}" + '\n')
        print(colored(f"Initial strength = {state.get_value(strength)}", 'red'))
        txt.write(f"Initial strength = {state.get_value(strength)}" + '\n')
        print(colored(f"Initial loot = {state.get_value(loot)} - Loot goal >= {loot_goal}", 'yellow'))
        txt.write(f"Initial loot = {state.get_value(loot)} - Loot goal >= {loot_goal}" + '\n')
        for ai in result.plan.actions:
            state = simulator.apply(state, ai)
            print(colored(f"Applied action {n_action}: ", 'grey') + str(ai) + ". ", end="")
            txt.write(f"Applied action {n_action}: {ai}. ")
            print(colored(f"Life: {state.get_value(life)}" , 'green') + " - " + colored(f"Strength: {state.get_value(strength)}" , 'red')+ " - " + colored(f"Loot: {state.get_value(loot)}", 'yellow'))
            txt.write(f"Life: {state.get_value(life)} - Strength: {state.get_value(strength)} - Loot: {state.get_value(loot)}\n")
            n_action += 1
        if simulator.is_goal(state):
            print(colored("Goal reached!", 'magenta'))
            txt.write("Goal reached!")

    txt.close()

    # Draw the graph with different colors for different types of edges
    edge_colors = ['xkcd:olive' if G[u][v]['type'] == 'normal' else 'xkcd:red' for u, v in G.edges()]

    node_colors = []
    treasure_node_colors = []
    enemy_node_colors = []
    weapon_node_colors = []
    potion_node_colors = []

    # Each type of room has a different color to be represented with
    for node in standard_rooms:
        if node in key_rooms:
            node_colors.append('xkcd:lightblue')
        elif node == start_room:
            node_colors.append('xkcd:green')
        elif node == exit_room:
            node_colors.append('gold')
        else:
            node_colors.append('xkcd:lavender')
    
    for node in treasure_rooms:
        if node in key_rooms:
            treasure_node_colors.append('xkcd:lightblue')
        elif node == exit_room:
            treasure_node_colors.append('gold')
        else:
            treasure_node_colors.append('xkcd:lavender')
    
    for node in enemy_rooms:
        if node in key_rooms:
            enemy_node_colors.append('xkcd:lightblue')
        elif node == exit_room:
            enemy_node_colors.append('gold')
        else:
            enemy_node_colors.append('xkcd:lavender')
    
    for node in weapon_rooms:
        if node in key_rooms:
            weapon_node_colors.append('xkcd:lightblue')
        elif node == exit_room:
            weapon_node_colors.append('gold')
        else:
            weapon_node_colors.append('xkcd:lavender')

    for node in potion_rooms:
        if node in key_rooms:
            potion_node_colors.append('xkcd:lightblue')
        elif node == exit_room:
            potion_node_colors.append('gold')
        else:
           potion_node_colors.append('xkcd:lavender')

    # Drawing the dungeon
    pos = nx.kamada_kawai_layout(G)
    enemy_nodes = nx.draw_networkx_nodes(G, pos, nodelist=list(enemy_rooms), node_size=1200, node_color=enemy_node_colors, node_shape ='h', linewidths=2)
    enemy_nodes.set_edgecolor('crimson')
    weapon_nodes = nx.draw_networkx_nodes(G, pos, nodelist=list(weapon_rooms), node_size=1000, node_color=weapon_node_colors, node_shape ='d', linewidths=2)
    weapon_nodes.set_edgecolor('xkcd:purple')
    potion_nodes = nx.draw_networkx_nodes(G, pos, nodelist=list(potion_rooms), node_size=700, node_color=potion_node_colors, node_shape ='s', linewidths=2)
    potion_nodes.set_edgecolor('xkcd:teal')
    treasure_nodes = nx.draw_networkx_nodes(G, pos, nodelist=list(treasure_rooms), node_size=2000, node_color=treasure_node_colors, node_shape ='*', linewidths=2)
    treasure_nodes.set_edgecolor('silver')
    nx.draw_networkx_nodes(G,pos, nodelist=standard_rooms, node_size=900, node_color=node_colors, node_shape = 'o')
    nx.draw_networkx_labels(G, pos, font_size=12, font_color="xkcd:ivory", font_weight='bold')
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=1.5)

    # Legend (different shapes and colors)
    legend_elements = [
        lines.Line2D([], [], color="xkcd:green", marker='o', markersize=12, linestyle=''),
        lines.Line2D([], [], color="gold", marker='o', markersize=12,linestyle='' ),
        lines.Line2D([], [], color="xkcd:lightblue", marker='o', markersize=12, linestyle=''),
        lines.Line2D([], [], color="xkcd:red"),
        lines.Line2D([], [], color="xkcd:lavender", marker='h', markersize=14, markeredgecolor='crimson', markeredgewidth=1.3, linestyle=''),
        lines.Line2D([], [], color="xkcd:lavender", marker='d', markersize=12, markeredgecolor='xkcd:purple', markeredgewidth=1.3, linestyle=''),
        lines.Line2D([], [], color="xkcd:lavender", marker='s', markersize=12, markeredgecolor='xkcd:teal', markeredgewidth=1.3, linestyle=''),
        lines.Line2D([], [], color="xkcd:lavender", marker='*', markersize=14, markeredgecolor='silver', markeredgewidth=1.3, linestyle='')
    ]
    legend_labels = [
        'Start room', 'Exit room', 'Key room', 'Closed door', 'Enemy room', 'Weapon room', 'Potion room', 'Treasure room'
    ]
    plt.legend(legend_elements, legend_labels, fontsize = 12)

    plt.get_current_fig_manager().full_screen_toggle() # Toggle fullscreen mode
    plt.show()

'''
Returns the farthest nodes inside the graph
'''
def farthest_node(G, start_room):
    shortest_paths = nx.single_source_shortest_path_length(G, start_room)

    # Find the node with maximum shortest path length
    max_length = -1
    farthest_node = None

    for target, length in shortest_paths.items():
        if length > max_length:
            max_length = length
            farthest_node = target

    return farthest_node

'''
Generates links between rooms as normal or door link.
'''
def generate_doors(G):
    door_probability = 0.4
    for u, v in G.edges():
        G[u][v]['type'] = random.choices(['normal', 'door'], weights=[1-door_probability, door_probability], k=1)[0]

'''
Generates keys in rooms and returns rooms with key
'''
def generate_keys(G, start_room, exit_room):
    key_rooms = []
    visited = set()
    queue = [start_room]
    door_count = 0

    while queue:
        room = queue.pop(0)
        visited.add(room)

        for u, v in G.edges(room):
            if G[u][v]['type'] == 'door':
                door_count += 1
                if door_count % 16 == 0:  # Only generate keys for 1/8 of the doors
                    temp_key_rooms = []
                    for neighbor in G.neighbors(room):
                        if neighbor in visited and neighbor not in key_rooms and neighbor != start_room and neighbor != exit_room:
                            temp_key_rooms.append(neighbor)
                    
                    if temp_key_rooms:
                        key_room = random.choice(temp_key_rooms)
                        key_rooms.append(key_room)
            elif v not in visited:
                queue.append(v)

    return key_rooms

'''
Generates treasures in rooms and returns rooms with treasure
'''
def generate_treasures(G, start_room, num_treasure_rooms):
    treasure_rooms = {}
    treasures_value = [10, 20, 30, 40]
    rooms_list = list(G)
    rooms_list.remove(start_room) # Remove start_room from list
     
    drawn_rooms = random.sample(rooms_list, num_treasure_rooms) # Draw num_treasure_rooms from rooms_list

    for room in drawn_rooms:
        selected_treasure = random.choice(treasures_value) # Draw 1 element from treasures_value
        treasure_rooms.update({room : selected_treasure})
    
    return treasure_rooms

'''
Generates loot goal
'''
def generate_loot_goal(treasure_rooms, loot_rate):
    sum = 0
    for room in treasure_rooms:
        sum += treasure_rooms[room]
    return (int)(sum * loot_rate)

'''
Generates enemies in rooms and returns rooms with enemy 
'''
def generate_enemies(G, start_room, num_enemy_rooms):
    enemy_rooms = {}
    enemies_value = [30, 50, 70, 90]
    room_list = list(G)
    room_list.remove(start_room) # Remove start_room from list

    drawn_rooms = random.sample(room_list, num_enemy_rooms) # Draw num_enemy_rooms from rooms_list

    for room in drawn_rooms:
        selected_enemy = random.choice(enemies_value) # Draw 1 element from enemies_value
        enemy_rooms.update({room : selected_enemy})
    
    return enemy_rooms

'''
Generates weapons in rooms and returns rooms with weapon
'''
def generate_weapons(G, start_room, enemy_rooms):
    weapons_rooms = {}
    rooms_list = list(G)
    
    available_rooms = [room for room in rooms_list if room not in list(enemy_rooms)] # Remove enemy_rooms from list
    available_rooms.remove(start_room) # Remove start_room from list
    
    for enemy in list(enemy_rooms):
        selected_room = random.choice(available_rooms) # Draw 1 room from available_rooms
        available_rooms.remove(selected_room) # Remove selected_room from list
        weapon_strength = enemy_rooms[enemy] # Set weapon_stregth to enemy_strength
        weapons_rooms.update({selected_room : weapon_strength})

    return weapons_rooms 

'''
Generates potions in rooms and returns rooms with potion 
'''
def generate_potions(G, start_room, num_potion_rooms):
    potion_rooms = {}
    potions_value = [10, 30, 50]
    room_list = list(G)
    room_list.remove(start_room) # Remove start_room from list

    drawn_rooms = random.sample(room_list, num_potion_rooms) # Draw num_potion_rooms from rooms_list

    for room in drawn_rooms:
        selected_potion = random.choice(potions_value) # Draw 1 element from potions_value
        potion_rooms.update({room : selected_potion})
    
    return potion_rooms   

'''
Choices yes or not (y/n) 
'''
def yes_or_no(question):
    incorrect_entry = True
    while incorrect_entry:
        choice = input(question + ' (y/n) ')
        if choice == 'y':
            incorrect_entry = False
            return True
        elif choice == 'n':
            incorrect_entry = False
            return False
        else:
             print(colored('Incorrect entry! Type \'y\' or \'n\'', 'light_red'))

def parse_arguments():
    parser = argparse.ArgumentParser( description = "Generate dungeon planning instance" )
    parser.add_argument( "--random_seed", required=False, help="Set RNG seed", default = "1229")
    parser.add_argument( "--num_rooms", required=False, help="Number of rooms in the dungeon", default = "30")

    args = parser.parse_args()
    args.random_seed = int(args.random_seed)
    if args.random_seed != None:
        random.seed( args.random_seed )
        print( ";;Setting seed to {0}\n".format(args.random_seed) )
    return args

def Main():
    args = parse_arguments()
    generate_instance('instance_'+str(args.num_rooms)+'_'+str(args.random_seed), int(args.num_rooms))

if __name__ == "__main__":
    Main()