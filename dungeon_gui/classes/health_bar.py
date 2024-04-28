import pygame

class HealthBar():
    def __init__(self, x=50, y=130, max_health=100):
        self.x = x
        self.y = y
        self.max_health = max_health
        self.current_health = max_health
        

    def draw(self, screen):
        # Draw the background of the health bar
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.max_health, 20))
        # Draw the current health
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x, self.y, self.current_health, 20))


    def update_health(self, health):
        self.current_health = health