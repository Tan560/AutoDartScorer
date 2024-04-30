import pygame
import sys
from pygame.locals import *

class MainScreen:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Dart Scoring Game")

        self.selected_game_mode = None

    def draw_checkbox(self, surface, x, y, width, height, checked):
        # Draw the checkbox rectangle
        pygame.draw.rect(surface, (0, 0, 0), (x, y, width, height), 2)

        # If checkbox is checked, draw the check mark
        if checked:
            pygame.draw.line(surface, (0, 0, 0), (x + 5, y + height // 2), (x + width // 2, y + height - 5), 2)
            pygame.draw.line(surface, (0, 0, 0), (x + width // 2, y + height - 5), (x + width - 5, y + 5), 2)

    def run(self):
        font = pygame.font.Font(None, 36)
        clock = pygame.time.Clock()

        checkbox_width, checkbox_height = 20, 20
        checkbox_x, checkbox_y = 100, 100
        checkbox_spacing = 50

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # Check if mouse click is within the checkboxes' area
                    if checkbox_x <= mouse_x <= checkbox_x + checkbox_width and \
                            checkbox_y <= mouse_y <= checkbox_y + checkbox_height:
                        self.selected_game_mode = "301"
                    elif checkbox_x <= mouse_x <= checkbox_x + checkbox_width and \
                            checkbox_y + checkbox_spacing <= mouse_y <= checkbox_y + checkbox_height + checkbox_spacing:
                        self.selected_game_mode = "501"
                    elif checkbox_x <= mouse_x <= checkbox_x + checkbox_width and \
                            checkbox_y + 2 * checkbox_spacing <= mouse_y <= checkbox_y + checkbox_height + 2 * checkbox_spacing:
                        self.selected_game_mode = "Cricket"

            self.screen.fill((110, 150, 150))

            # Draw the checkboxes
            self.draw_checkbox(self.screen, checkbox_x, checkbox_y, checkbox_width, checkbox_height, self.selected_game_mode == "301")
            self.draw_checkbox(self.screen, checkbox_x, checkbox_y + checkbox_spacing, checkbox_width, checkbox_height, self.selected_game_mode == "501")
            self.draw_checkbox(self.screen, checkbox_x, checkbox_y + 2 * checkbox_spacing, checkbox_width, checkbox_height, self.selected_game_mode == "Cricket")

            # Draw the game mode texts
            text_301 = font.render("301", True, (0, 0, 0))
            self.screen.blit(text_301, (checkbox_x + checkbox_width + 10, checkbox_y))

            text_501 = font.render("501", True, (0, 0, 0))
            self.screen.blit(text_501, (checkbox_x + checkbox_width + 10, checkbox_y + checkbox_spacing))

            text_cricket = font.render("Cricket", True, (0, 0, 0))
            self.screen.blit(text_cricket, (checkbox_x + checkbox_width + 10, checkbox_y + 2 * checkbox_spacing))

            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    pygame.init()
    mainScreen = MainScreen()
    mainScreen.run()
