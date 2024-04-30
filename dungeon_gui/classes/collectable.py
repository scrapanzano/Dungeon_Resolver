
class Collectable():
    def __init__(self):
        self.alpha = 255
        self.collected = False

    def render_collectable(self):
        pass

    def collect(self):
        self.collected = True