from unified_planning.shortcuts import *
from termcolor import colored

class GUI():
    def __init__(self, problem, result, rooms):
        self.problem = problem
        self.result = result
        self.rooms = rooms

    def run(self):
        
        # QUI ANDRA' INSERITO IL MAIN LOOP DI DUNGEON_GUI

        # Prova problem & result: stampa sequential simulator
        # Invoke unified-planning sequential simulator
        life = FluentExp(self.problem.fluent("hero_life"))
        strength = FluentExp(self.problem.fluent("hero_strength"))
        loot = FluentExp(self.problem.fluent("hero_loot"))
        n_action = 1
        with SequentialSimulator(self.problem) as simulator: 
            state = simulator.get_initial_state()
            print(colored(f"Initial life = {state.get_value(life)}", 'green'))
            print(colored(f"Initial strength = {state.get_value(strength)}", 'red'))
            print(colored(f"Initial loot = {state.get_value(loot)}", 'yellow'))
            for ai in self.result.plan.actions:
                state = simulator.apply(state, ai)
                print(colored(f"Applied action {n_action}: ", 'grey') + str(ai) + ". ", end="")
                print(colored(f"Life: {state.get_value(life)}" , 'green') + " - " + colored(f"Strength: {state.get_value(strength)}" , 'red')+ " - " + colored(f"Loot: {state.get_value(loot)}", 'yellow'))
                n_action += 1
            if simulator.is_goal(state):
                print(colored("Goal reached!", 'magenta'))

        # Prova room_list: stampa oggetti in rooms
        for room in self.rooms:
            print(room)

