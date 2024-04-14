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

template_name = "./progetto/dungeon_template.pddl"

def generate_instance(instance_name, num_rooms):
    with open( template_name ) as instream :
        text = instream.read()
        template = string.Template( text )
    template_mapping = dict()
    template_mapping['instance_name'] = instance_name
    template_mapping['domain_name'] = 'simple_dungeon'

    # Generate a random dungeon in which each room is connected at least with another one
    G = nx.connected_watts_strogatz_graph(num_rooms, k=4, p=0.1)

    # Start room chosen randomly 
    start_room = random.choice(list(G.nodes))

    # Exit room (cannot be the start_room)
    exit_room = generate_exit_room(G, start_room)

    # List of rooms in which there's a key and a reference of which door that key can open
    key_rooms = generate_keys(G, start_room, exit_room)

    # Creating the string that containts the room_list
    room_list = ''

    for i in range(num_rooms):
        room_list += 'R' + str(i) + ' '

    # Creating the string that contains the key_list
    key_list = ''
    
    for i in range(len(key_rooms)):
        key_list += 'K' + str(i+1) + ' '

    # Creating the string that describes how all the rooms are connected with each others
    room_links = ''

    for room in G.nodes:
        for neighbor in G.neighbors(room):
            room_links += '(connected R' + str(room) + ' R' + str(neighbor) + ') ' 

    # Creating the string that describes the doors between rooms and the locations of each key
    closed_doors = ''
    keys_location = ''
    index = 1

    for key in key_rooms:
        room_1, room_2 = key
        closed_doors += '(closed_door R' + str(room_1) + ' R' + str(room_2) + ' K' + str(index) + ') '
        keys_location += '(key_at K' + str(index) + ' R' + str(key_rooms.get(key)) + ')'
        index += 1


    # Draw the graph with different colors for different types of edges
    edge_colors = ['blue' if G[u][v]['type'] == 'normal' else 'red' for u, v in G.edges()]

    node_colors = []

    # Each type of room has a different color to be represented with
    for node in G.nodes():
        if node in key_rooms.values():
            node_colors.append('grey')
        elif node == start_room:
            node_colors.append('green')
        elif node == exit_room:
            node_colors.append('gold')
        else:
            node_colors.append('blue')
    
    
    # Objects
    template_mapping['room_list'] = room_list
    template_mapping['key_list'] = key_list
    # Init
    template_mapping['start_room'] = '(at R' + str(start_room) + ')'
    template_mapping['exit_room'] = '(exit_room R' + str(exit_room) + ')'
    template_mapping['room_links'] = room_links
    template_mapping['closed_doors'] = closed_doors
    template_mapping['keys_location'] = keys_location

    f = open('./progetto/simple_dungeon_problem.pddl', 'w')
    f.write(str(template.substitute(template_mapping)))
    f.close

    nx.draw(G, with_labels=True, edge_color=edge_colors, node_color=node_colors)
    plt.show()

def generate_keys (G, start_room, exit_room):
    key_rooms = {}

    for u, v in G.edges():
        # Assign a random type (normal edge or door edge) to each edge with different probabilities
        G[u][v]['type'] = random.choices(['normal', 'door'], weights=[0.8, 0.2], k=1)[0]
        if G[u][v]['type'] == 'door':
            # If the edge is a door edge, assign to one of the neighbors of the two rooms a key
            # Neighbor is chosen randomly among the neighbors that are not connected to the selected room
            room = random.choice([u, v])
            temp_key_rooms = []
            for neighbor in G.neighbors(room):
                if room == u and neighbor != v and neighbor not in G.neighbors(v) and neighbor not in key_rooms.values() and neighbor != start_room and neighbor != exit_room:
                    temp_key_rooms.append(neighbor)
                elif room == v and neighbor != u and neighbor not in G.neighbors(u) and neighbor not in key_rooms.values() and neighbor != start_room and neighbor != exit_room:
                    temp_key_rooms.append(neighbor)
            
            if temp_key_rooms:
                key_room = random.choice(temp_key_rooms)
                key_rooms[(u,v)] = key_room
    return key_rooms

    
def generate_exit_room(G, start_room):
    found = False
    while not found:
        exit_room = random.choice(list(G.nodes))
        if exit_room != start_room and exit_room not in G.neighbors(start_room):
            found = True
    return exit_room

def parse_arguments():
    parser = argparse.ArgumentParser( description = "Generate dungeon planning instance" )
    parser.add_argument( "--random_seed", required=False, help="Set RNG seed", default = "1229")
    parser.add_argument( "--num_rooms", required=True, help="Number of rooms in the dungeon", default = "5")

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