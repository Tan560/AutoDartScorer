import pygame
from pygame.locals import *

class gameMode:
    def __init__(self):
        pass

    def calculate_score(self, dart_position):
        pass

    def game_mode_screen(self):
        # Create a new screen with black background
        self.target_width = 1920
        self.target_height = 1080
        self.screen = pygame.display.set_mode((self.target_width, self.target_height), RESIZABLE)  # Initial resolution

        self.scale_factor = 1.5  # Scale factor for resizing elements
        self.screen.fill((0, 0, 0))

        # Create font object with green color
        self.font = pygame.font.Font(None, 36)

        # Draw "Back" button
        self.back_button_text = self.font.render("Back", True, (225, 225, 190))
        self.back_button_rect = self.back_button_text.get_rect(topright=(self.target_width - 20, 20))

        # Make the button bigger
        self.back_button_rect.inflate_ip(50, 20)

        # Update the display
        pygame.display.flip()

class gameMode301(gameMode):
    def __init__(self):
        super().__init__()

    def calculate_score(self, dart_position):
        return super().calculate_score(dart_position)

    def game_mode_screen(self):
        super().game_mode_screen()

        running = True # Wait for user input before returning to the main screen (Main loop)
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and self.back_button_rect.collidepoint(event.pos):  # Left mouse button clicked
                    running = False
            
            modeText = self.font.render("Game Mode: 301", True, (0, 255, 0))
            modeText_rect = modeText.get_rect(center=(self.target_width / 2,50))

            # Blit the text onto the screen
            self.screen.blit(modeText, modeText_rect)
            
            # Update button color when mouse hovers over it
            if self.back_button_rect.collidepoint(pygame.mouse.get_pos()):
                button_color = (255, 25, 25)  # Darker color when mouse hovers over button
            else:
                button_color = (255, 0, 0)  # Default color
                
            # Draw button with updated color
            pygame.draw.rect(self.screen, button_color, self.back_button_rect)
            self.back_button_text_rect = self.back_button_text.get_rect(center=self.back_button_rect.center)
            self.screen.blit(self.back_button_text, self.back_button_text_rect)
            pygame.display.flip()

class gameMode501(gameMode):
    def __init__(self):
        super().__init__()

    def calculate_score(self, dart_position):
        return super().calculate_score(dart_position)

    def game_mode_screen(self):
        super().game_mode_screen()

class gameModeCricket(gameMode):
    def __init__(self):
        super().__init__()

    def calculate_score(self, dart_position):
        return super().calculate_score(dart_position)

    def game_mode_screen(self):
        super().game_mode_screen()
