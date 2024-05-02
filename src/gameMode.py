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
    def __init__(self, teams):
        super().__init__()
        self.teams = teams
        print(self.teams)
        self.teamScores = {team: 301 for team in teams if team != ''}
        print(self.teamScores)

    def calculate_score(self, dart_position):
        return super().calculate_score(dart_position)

    def display_teams(self):
        # Display teams and scores in 5x2 arrangement
        x_offset = 1200  # X-coordinate offset for displaying teams
        y_offset = 100  # Y-coordinate offset for displaying teams
        row_spacing = 50  # Spacing between rows
        col_spacing = 100  # Spacing between columns
        max_teams_per_row = 5
        max_rows = 2
        current_row = 0
        current_col = 0

        for team, score in self.teamScores.items():
            if current_row >= max_rows:
                break

            team_text = self.font.render(f"{team}: {score}", True, (255, 255, 255))
            team_text_rect = team_text.get_rect(topleft=(x_offset + current_col * col_spacing, y_offset + current_row * row_spacing))
            self.screen.blit(team_text, team_text_rect)

            current_col += 1
            if current_col >= max_teams_per_row:
                current_row += 1
                current_col = 0
                
    def game_mode_screen(self):
        super().game_mode_screen()

        # Display current team and their score in larger font
        current_team = self.teams[0]
        current_score = self.teamScores[current_team]        
        
        running = True # Wait for user input before returning to the main screen (Main loop)
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and self.back_button_rect.collidepoint(event.pos):  # Left mouse button clicked
                    running = False
            
            current_team_text = self.font.render(f"Current Team: {current_team} - Score: {current_score}", True, (255, 255, 255))
            current_team_text_rect = current_team_text.get_rect(center=(self.target_width / 2, 200))
            self.screen.blit(current_team_text, current_team_text_rect)

            # Display all teams and their scores
            self.display_teams()
            
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

        running = True # Wait for user input before returning to the main screen (Main loop)
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN and event.button == 1 and self.back_button_rect.collidepoint(event.pos):  # Left mouse button clicked
                    running = False
            
            modeText = self.font.render("Game Mode: 501", True, (0, 255, 0))
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

class gameModeCricket(gameMode):
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
            
            modeText = self.font.render("Game Mode: Cricket", True, (0, 255, 0))
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
