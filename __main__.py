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

def generate_instance(instance_name, num_rooms):
    with open( template_name ) as instream :
        text = instream.read()
        template = string.Template( text )

    # Generate a random dungeon in which each room is connected at least with another one
    G = nx.connected_watts_strogatz_graph(num_rooms, k=4, p=0.1)
    
    start_room = 0

    exit_room = farthest_node(G, start_room)

    generate_doors(G)

    # List of rooms in which there's a key and a reference of which door that key can open
    key_rooms = generate_keys(G, start_room, exit_room)

    # Generate the loot that will be placed in the dungeon
    loot_rooms = generate_loot(G, start_room)

    # Creating the string that containts the room_list
    room_list = ''

    for i in range(num_rooms):
        room_list += 'R' + str(i) + ' '

    # Creating the string that containts the treasures_list
    treasures_list = ''

    for i in range(len(loot_rooms)):
        treasures_list += 'T' + str(i) + ' '

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

    keys_location = ''

    for key_room in key_rooms:
        keys_location += '(key_at R' + str(key_room) + ') '


    treasures_location = ''
    treasures_value = ''
    index = 0
    total_loot = 0

    for room in loot_rooms:
        treasures_location += '(treasure_at T' + str(index) + ' R' + str(room) + ') '
        treasures_value += '( = (treasure_value T' + str(index) + ') ' + str(loot_rooms[room]) + ') '
        total_loot += loot_rooms[room]
        index += 1

    loot_goal = loot_goal = math.ceil(total_loot * 0.75)  
    print("Total loot:", total_loot)
    print("Loot goal:", loot_goal)
    
    # Populate the template
    template_mapping = dict()
    template_mapping['instance_name'] = instance_name
    template_mapping['domain_name'] = 'simple_dungeon'
    # Objects
    template_mapping['room_list'] = room_list
    template_mapping['treasures_list'] = treasures_list
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
    template_mapping['loot_goal'] = str(loot_goal)

    f = open('./dungeon_resolver/simple_dungeon_problem.pddl', 'w')
    f.write(str(template.substitute(template_mapping)))
    f.close()

    #os.system("java -jar Dungeon_Resolver/enhsp.jar -o Dungeon_Resolver/simple_dungeon_domain.pddl -f Dungeon_Resolver/simple_dungeon_problem.pddl -planner opt-hrmax")

    # Using unified-planning for reading the domain and instance files
    reader = PDDLReader()
    problem = reader.parse_problem("./dungeon_resolver/simple_dungeon_domain.pddl", "./dungeon_resolver/simple_dungeon_problem.pddl")

    up.shortcuts.get_environment().credits_stream = None

    # Invoke a unified-planning planner 
    with OneshotPlanner(name='enhsp') as planner:
        result = planner.solve(problem)
        print("%s returned: %s" % (planner.name, result.plan))

    # loot = FluentExp(problem.fluent("hero_loot"))
    # with SequentialSimulator(problem) as simulator: 
    #     state = simulator.get_initial_state()
    #     print(f"Initial loot = {state.get_value(loot)}")
    #     for ai in result.plan.actions:
    #         state = simulator.apply(state, ai)
    #         print(f"Applied action: {ai}. ", end="")
    #         print(f"Loot: {state.get_value(loot)}")
    #     if simulator.is_goal(state):
    #         print("Goal reached!")

    # Draw the graph with different colors for different types of edges
    edge_colors = ['blue' if G[u][v]['type'] == 'normal' else 'red' for u, v in G.edges()]

    node_colors = []

    # Each type of room has a different color to be represented with
    for node in G.nodes():
        if node in key_rooms:
            node_colors.append('grey')
        elif node == start_room:
            node_colors.append('green')
        elif node == exit_room:
            node_colors.append('gold')
        else:
            node_colors.append('blue')

    # Drawing the dungeon 
    nx.draw_kamada_kawai(G, with_labels=True, edge_color=edge_colors, node_color=node_colors)
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

def generate_doors(G):
    door_probability = 0.4
    for u, v in G.edges():
        G[u][v]['type'] = random.choices(['normal', 'door'], weights=[1-door_probability, door_probability], k=1)[0]

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
                if door_count % 16 == 0:  # Only generate keys for half of the doors
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
   
def generate_exit_room(G, start_room):
    found = False
    while not found:
        exit_room = random.choice(list(G.nodes))
        if exit_room != start_room and exit_room not in G.neighbors(start_room):
            found = True
    return exit_room

def generate_loot(G, start_room):
    loot = [5, 10, 15, 20]
    loot_weights = [0.4, 0.3, 0.2, 0.1]  # probabilities for each loot value
    loot_rooms = {}
    spawn_probability = 0.2
    for room in G.nodes:
        if room != start_room:
            if random.random() < spawn_probability:  # Spawn loot with a certain probability
                loot_rooms[room] = random.choices(loot, weights=loot_weights, k=1)[0]  # Assign a random loot value from loot
    return loot_rooms   

def parse_arguments():
    parser = argparse.ArgumentParser( description = "Generate dungeon planning instance" )
    parser.add_argument( "--random_seed", required=False, help="Set RNG seed", default = "42")
    parser.add_argument( "--num_rooms", required=False, help="Number of rooms in the dungeon", default = "100")

    args = parser.parse_args()
    args.random_seed = int(args.random_seed)
    if args.random_seed != None:
        random.seed( args.random_seed )
        print( ";;Setting seed to {0}".format(args.random_seed) )
    return args

def Main():
    args = parse_arguments()
    generate_instance('instance_'+str(args.num_rooms)+'_'+str(args.random_seed), int(args.num_rooms))

if __name__ == "__main__":
    Main()