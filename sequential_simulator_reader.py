import re

def extract_number(str):
    string = str.split()
    for element in string:
        if element.isdigit():
            return element

def extract_numbers(str):
    numbers = []
    string = str.split()
    for element in string:
        if element.isdigit():
            numbers.append(element)
    return numbers

def extract_rooms(str):
    rooms = re.findall("r[0-9][0-9]|r[0-9]", str)
    return rooms


with open('./dungeon_resolver/sequential_simulator.txt', 'r') as instream:
    lines = instream.readlines()
    for line in lines:
        if 'Initial life' in line:
            life = extract_number(line)
            print(f'Life = {life}')
        elif 'Initial strength' in line:
            strength = extract_number(line)
            print(f'Strength = {strength}')
        elif 'Initial loot' in line:
            loot = extract_number(line)
            print(f'Loot = {loot}')
        elif 'Applied action' in line:
            if 'move' in line:
                rooms = extract_rooms(line)
                print('Move action')
                print(rooms)
            elif 'collect_weapon' in line:
                print('Collect weapon action')
            elif 'collect_treasure' in line:
                print('Collect treasure action')
            elif 'collect_potion' in line:
                print('Collect potion action')
            elif 'drink_potion' in line:
                print('Drink potion action')
            elif 'defeat_enemy' in line:
                print('Defeat enemy action')
            elif 'escape_from_dungeon' in line:
                print('Escape action')
            
            numbers = extract_numbers(line)
            life = numbers[0]
            strength = numbers[1]
            loot = numbers[2]
            print(f'Life = {life} - Strenght = {strength} - Loot = {loot}')
    
