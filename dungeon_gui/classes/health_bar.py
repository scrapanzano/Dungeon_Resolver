import pygame

class HealthBar():
    def __init__(self, blink_counter, x=50, y=130, max_health=100):
        self.x = x
        self.y = y
        self.max_health = max_health
        self.current_health = max_health
        self.blink_counter = blink_counter
        self.blinking = False
        

    def draw(self, screen):
        if self.blinking and self.blink_counter % 2 == 0:
            # Create a new Surface for the health bar
            health_bar_surface = pygame.Surface((self.max_health, 20))
            # Fill the Surface with the desired color
            health_bar_surface.fill((255, 100, 100))
            # Blit the Surface onto the screen with the BLEND_RGBA_MULT flag
            screen.blit(health_bar_surface, (self.x, self.y), special_flags=pygame.BLEND_RGBA_MULT)
        else:
            # Draw the background of the health bar
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.max_health, 20))
            # Draw the current health
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x, self.y, self.current_health, 20))


    def update_health(self, health):
        self.current_health = health
        self.blinking = True