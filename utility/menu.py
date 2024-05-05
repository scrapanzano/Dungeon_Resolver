
"""
This module is part of the utility package, which contains some functions and utility classes
"""

from utility.title import print_title
from termcolor import colored

EXIT_ITEM = '0 - Exit'
CHOOSE_ITEM = 'Enter the number of the desired option --> '

class Menu():
    """
    This class representat a Menu Object 
    """

    def __init__(self, title, menu_items):
        self.title = title
        self.menu_items = menu_items


    def print_menu(self):
        """
        Print a Menu composed by a title and different items
        """
        print_title()
        print('\n' + self.title + '\n')
        i = 1
        for item in self.menu_items:
            print(str(i) + ' - ' + item)
            i += 1
        print('\n' + EXIT_ITEM + '\n')


    def choose(self):
        """
        Allows to enter a choice between different menu items
        
        Returns
        -------
        :returns: Number of entered choice
        :rtype: int
        """
        self.print_menu()

        incorrect_entry = True
        while(incorrect_entry):
            choice = input(CHOOSE_ITEM)
            n_choice = int (choice)
            if n_choice >= 0 and n_choice <= len(self.menu_items):
                incorrect_entry = False
            else:
                print(colored(f'Incorrect entry! Type a number between 0 and {len(self.menu_items)}', 'light_red'))
        
        return n_choice    
