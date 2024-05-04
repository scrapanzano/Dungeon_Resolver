# Dungeon Resolver

Dungeon Resolver is a project developed initially as a university assignment for the "Intelligent Systems" course, focusing on Automated Planning. The project utilizes the unified-planning library to implement a planner and simulator for resolving randomly generated dungeon instances.

## Introduction

Automated Planning is a field within Artificial Intelligence (AI) that deals with designing algorithms and systems capable of generating plans to achieve specific goals. In the context of Dungeon Resolver, the objective is to create a system that can navigate through a randomly generated dungeon, overcoming obstacles, enemies, and collecting resources along the way.

## Features

- **Random Dungeon Generation**: The program creates random dungeon instances with various rooms containing weapons, enemies, potions, and loot. This ensures each run provides a unique challenge.
  
- **Unified-Planning Planner**: Dungeon Resolver employs the unified-planning library to implement the planner. The planner, named "enhsp", is responsible for generating a plan to navigate through the dungeon efficiently.

- **Plan Representation**: Once a plan is generated, it is represented visually using a graphical user interface (GUI). The GUI simulates a 2D top-down game, providing a clear visualization of the plan in action.

## Usage

To use Dungeon Resolver, follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary dependencies, including the unified-planning library.
3. Run the program and specify the parameters for dungeon generation.
4. The planner will then generate a plan (if exits) for navigating through the dungeon.
5. At the user's choice plan will be displayed in the GUI, allowing the user to visualize the execution steps.
6. At the user's choice the dungeon structure will be plotted using networkx graph.

## Getting Started

To get started with Dungeon Resolver, you can follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/scrapanzano/dungeon_resolver.git
```

2. Install dependencies:

```bash
cd .\dungeon_resolver
pip install -r requirements.txt [Windows OS]
pip3 install -r requirements.txt [Mac OS]
```

3. Run the program:

```bash
python3 .\dungeon_resolver\generate_dungeon_problem.py
```

4. Follow the on-screen instructions to specify dungeon parameters and visualize the plan.

## Documentation
The documentation is available [here]().

## Contributors

- [Davide Leone](https://github.com/scrapanzano)
- [Mattia Zavaglio](https://github.com/matuz91zava)

## Acknowledgments
The unified-planning library contributors for providing the planner.
