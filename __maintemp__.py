import sys
import os
import argparse
import math
import random
import string
from string import Template
import networkx as nx
import matplotlib.pyplot as plt
from unified_planning.shortcuts import *
from unified_planning.io import PDDLReader

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
    treasure_probability = 0.3 # 30%
    num_treasure_rooms = (int)(num_rooms * treasure_probability) 
    treasure_rooms = generate_treasures(G, start_room, num_treasure_rooms)

    # List of rooms in which there's not a treasure 
    no_treasure_rooms = []
    for node in G.nodes():
        if node not in list(treasure_rooms):
            no_treasure_rooms.append(node)

    # Generating loot_goal
    loot_rate = 0.5 # 50%
    loot_goal = generate_loot_goal(treasure_rooms, loot_rate)

    # Creating the string that containts the room_list
    room_list = ''

    for i in range(num_rooms):
        room_list += 'R' + str(i) + ' '

    # Creating the string that contains the treasure_list
    treasure_list = ''

    for i in range(len(treasure_rooms)):
        treasure_list += 'T' + str(i) + ' '

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

    # Creating the string that containts the keys location
    keys_location = ''

    for key_room in key_rooms:
        keys_location += '(key_at R' + str(key_room) + ') '

    # Creating the string that containts the treasures location and the treasures value
    treasures_location = ''
    treasures_value = ''
    index = 0

    for room in treasure_rooms:
        treasure_name = 'T' + str(index) + ' '
        treasure_value = treasure_rooms[room]
        treasures_location += '(treasure_at ' + treasure_name + 'R' + str(room) + ') '
        treasures_value += '(= (treasure_value ' + treasure_name + ') ' + str(treasure_value) +') '
        index += 1
    
    # Populate template
    template_mapping = dict()
    template_mapping['instance_name'] = instance_name
    template_mapping['domain_name'] = 'simple_dungeon' 
    # Objects
    template_mapping['room_list'] = room_list
    template_mapping['treasures_list'] = treasure_list
    # Init
    template_mapping['start_room'] = '(at R' + str(start_room) + ')'
    template_mapping['exit_room'] = '(exit_room R' + str(exit_room) + ')'
    template_mapping['room_links'] = room_links
    template_mapping['closed_doors'] = closed_doors
    template_mapping['keys_location'] = keys_location
    template_mapping['key_counter'] = '(= (key_counter) 0)'
    template_mapping['treasures_location'] = treasures_location
    template_mapping['treasures_value'] = treasures_value
    template_mapping['hero_loot'] = '(= (hero_loot) 0)'
    #Goal
    template_mapping['loot_goal'] = str(loot_goal) 

    # Write file
    f = open('./dungeon_resolver/simple_dungeon_problem.pddl', 'w')
    f.write(str(template.substitute(template_mapping)))
    f.close()

    # os.system("java -jar Dungeon_Resolver/enhsp.jar -o temp/simple_dungeon_domain.pddl -f temp/simple_dungeon_problem.pddl -planner opt-hrmax")

    # Using unified-planning for reading the domain and instance files
    reader = PDDLReader()
    problem = reader.parse_problem("./dungeon_resolver/simple_dungeon_domain.pddl", "./dungeon_resolver/simple_dungeon_problem.pddl")
    
    # Invoke unified-planning planner enhsp
    up.shortcuts.get_environment().credits_stream = None # Disable printing of planning engine credits

    with OneshotPlanner(name='enhsp') as planner:
        result = planner.solve(problem)
        print("%s returned: %s\n" % (planner.name, result.plan))

    # Invoke unified-planning sequential simulator
    loot = FluentExp(problem.fluent("hero_loot"))
    with SequentialSimulator(problem) as simulator: 
        state = simulator.get_initial_state()
        print(f"Initial loot = {state.get_value(loot)}")
        for ai in result.plan.actions:
            state = simulator.apply(state, ai)
            print(f"Applied action: {ai}. ", end="")
            print(f"Loot: {state.get_value(loot)}")
        if simulator.is_goal(state):
            print("Goal reached!")

    # Draw the graph with different colors for different types of edges
    edge_colors = ['blue' if G[u][v]['type'] == 'normal' else 'red' for u, v in G.edges()]

    node_colors = []
    treasure_node_colors = []
        
    # Each type of room has a different color to be represented with
    for node in no_treasure_rooms:
        if node in key_rooms:
            node_colors.append('grey')
        elif node == start_room:
            node_colors.append('green')
        elif node == exit_room:
            node_colors.append('gold')
        else:
            node_colors.append('blue')
    
    for node in treasure_rooms:
        if node in key_rooms:
            treasure_node_colors.append('grey')
        elif node == exit_room:
            treasure_node_colors.append('gold')
        else:
            treasure_node_colors.append('blue')

    # Drawing the dungeon (different shape for treasure_rooms)
    nx.draw_kamada_kawai(G, nodelist=list(treasure_rooms), node_size=900, node_color=treasure_node_colors, node_shape ='*', edge_color=edge_colors)
    nx.draw_kamada_kawai(G, nodelist=no_treasure_rooms, node_size=400, node_color=node_colors, node_shape = 'o', edge_color=edge_colors)
    nx.draw_networkx_labels(G, pos=nx.kamada_kawai_layout(G), font_size=12, font_color="white")
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
Generates treasure in rooms and returns rooms with treasure
'''
def generate_treasures(G, start_room, num_treasure_rooms):
    treasure_rooms = {}
    treasures_value = [10, 20, 30, 40]
    rooms_list = list(G)
    rooms_list.remove(start_room) # Remove start_room from list
     
    drawn_rooms = random.sample(rooms_list, num_treasure_rooms) # Draw num_treasure_rooms from rooms_list

    for room in drawn_rooms:
        selected_treasure = random.sample(treasures_value, 1) # Draw 1 element from treasures_value
        treasure_rooms.update({room : selected_treasure[0]})
    
    return treasure_rooms

'''
Generates loot goal
'''
def generate_loot_goal(treasure_rooms, loot_rate):
    sum = 0
    for room in treasure_rooms:
        sum += treasure_rooms[room]
    return (int)(sum * loot_rate)

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