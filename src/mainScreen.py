import pygame
import sys
from GameMode import GameMode301, GameMode501, GameModeCricket

class MainScreen:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Dart Scoring Game")

        self.game_mode = None  # Placeholder for the selected game mode

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:  # Press 1 for 301 game mode
                        self.game_mode = GameMode301()
                    elif event.key == pygame.K_2:  # Press 2 for 501 game mode
                        self.game_mode = GameMode501()
                    elif event.key == pygame.K_3:  # Press 3 for Cricket game mode
                        self.game_mode = GameModeCricket()

            self.screen.fill((255, 255, 255))  # Fill screen with white color
            # Add main screen elements (buttons, text, etc.) here

            pygame.display.flip()  # Update the display
