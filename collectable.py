
"""
This module is part of the dungeon_gui package, for the graphical representation of the dungeon
"""

class Collectable():
    """
    This is the superclass for all Collectable Objects
    """

    def __init__(self):
        self.alpha = 255
        self.collected = False


    def render_collectable(self):
        """
        Rendering of Collectable Object, implemented in all Collectable Class
        """
        pass


    def collect(self):
        """
        Sets the collected attribute for the Object to True
        """
        self.collected = True