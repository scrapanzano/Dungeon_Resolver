import pygame

class HealthBar():
    def __init__(self, x=50, y=40, max_health=100):
        self.x = x
        self.y = y
        self.max_health = max_health
        self.current_health = max_health - 30
        self.font = pygame.font.Font("dungeon_Resolver/dungeon_gui/Minecraft.ttf", 20)  # Use the default font

    def draw(self, screen):
        # Draw the background of the health bar
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.max_health, 20))
        # Draw the current health
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x, self.y, self.current_health, 20))

        # Render the label
        label = self.font.render(f"{self.current_health}/{self.max_health}", True, (0, 0, 0))

        # Calculate the position of the label
        label_rect = label.get_rect(center=(self.x + self.max_health // 2, self.y + 20 // 2))

    # Adjust the y-coordinate of the center of the label to vertically center it within the health bar
        label_rect.centery = self.y + 10

        # Draw the label
        screen.blit(label, label_rect)

    def update(self, health):
        self.current_health = health