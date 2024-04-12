import sys
import os
import argparse
import math
import random
import string
from string import Template
import networkx as nx
import matplotlib.pyplot as plt

template_name = "./progetto/dungeon_template.pddl"

def generate_instance(instance_name, num_rooms):
    with open( template_name ) as instream :
        text = instream.read()
        template = string.Template( text )
    template_mapping = dict()
    template_mapping['instance_name'] = instance_name
    template_mapping['domain_name'] = 'dungeon'

    # Generate a random dungeon in which each room is connected at least with another one
    G = nx.connected_watts_strogatz_graph(num_rooms, k=4, p=0.1)

    
    for u, v in G.edges():
        # Assign a random type (normal edge or door edge) to each edge with different probabilities
        G[u][v]['type'] = random.choices(['normal', 'door'], weights=[0.7, 0.3], k=1)[0]
        if G[u][v]['type'] == 'door':
            # If the edge is a door edge, assign to one of the neighbors of the two rooms a key
            # Neighbor is chosen randomly among the neighbors that are not connected to the selected room
            room = random.choice([u, v])
            key_rooms = {}
            temp_key_rooms = []
            for neighbor in G.neighbors(room):
                if room == u and neighbor != v and neighbor not in G.neighbors(v) and neighbor not in key_rooms.values():
                    temp_key_rooms.append(neighbor)
                elif room == v and neighbor != u and neighbor not in G.neighbors(u) and neighbor not in key_rooms.values():
                    temp_key_rooms.append(neighbor)
            
            if temp_key_rooms:
                key_room = random.choice(temp_key_rooms)
                key_rooms[(u, v)] = key_room 
   

    # Draw the graph with different colors for different types of edges
    edge_colors = ['blue' if G[u][v]['type'] == 'normal' else 'red' for u, v in G.edges()]

    # Draw the graph with different colors for different types of nodes
    node_colors = ['gold' if node in key_rooms.values() else 'blue' for node in G.nodes()]
    
    nx.draw(G, with_labels=True, edge_color=edge_colors, node_color=node_colors)
    plt.show()









    print(template.substitute(template_mapping))

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