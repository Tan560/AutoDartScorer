import pygame
import sys
from pygame.locals import *

class MainScreen:
    def __init__(self):
        self.target_width = 1920
        self.target_height = 900
        self.screen = pygame.display.set_mode((self.target_width, self.target_height), RESIZABLE)  # Initial resolution
        pygame.display.set_caption("Dart Scoring Game")

        self.selected_game_mode = None
        self.scale_factor = 1.5  # Scale factor for resizing elements
        self.label_font_size = 36
        self.checkbox_size = 20
        self.spacing = 30

        self.font = pygame.font.Font(None, int(self.label_font_size * self.scale_factor))
        self.clock = pygame.time.Clock()

        self.text_fields = ["" for _ in range(10)]
        self.active_text_field = None

        # Button properties
        self.button_width = 120
        self.button_height = 50
        self.start_button_rect = pygame.Rect(1000 * self.scale_factor, 300 * self.scale_factor, self.button_width * self.scale_factor, self.button_height * self.scale_factor)
        self.reset_button_rect = pygame.Rect(1000 * self.scale_factor, 400 * self.scale_factor, self.button_width * self.scale_factor, self.button_height * self.scale_factor)

    def draw_checkbox(self, surface, x, y, checked):
        # Draw the checkbox rectangle
        pygame.draw.rect(surface, (0, 0, 0), (x, y, int(self.checkbox_size * self.scale_factor), int(self.checkbox_size * self.scale_factor)), 2)

        # If checkbox is checked, draw the check mark
        if checked:
            pygame.draw.line(surface, (0, 0, 0), (x + 5 * self.scale_factor, y + (self.checkbox_size // 2) * self.scale_factor), (x + (self.checkbox_size // 2) * self.scale_factor, y + self.checkbox_size * self.scale_factor - 5 * self.scale_factor), 2)
            pygame.draw.line(surface, (0, 0, 0), (x + (self.checkbox_size // 2) * self.scale_factor, y + self.checkbox_size * self.scale_factor - 5 * self.scale_factor), (x + self.checkbox_size * self.scale_factor - 5 * self.scale_factor, y + 5 * self.scale_factor), 2)

    def update_layout(self):
        # Update scale factor based on window size relative to the target resolution
        self.scale_factor = min(self.screen.get_width() / self.target_width, self.screen.get_height() / self.target_height)

        # Update font size and checkbox size based on scale factor
        self.font = pygame.font.Font(None, int(self.label_font_size * self.scale_factor))
        self.checkbox_size = int(20 * self.scale_factor)

        # Update button sizes and positions based on scale factor
        self.start_button_rect = pygame.Rect(1500 * self.scale_factor, 100 * self.scale_factor, self.button_width * self.scale_factor, self.button_height * self.scale_factor)
        self.reset_button_rect = pygame.Rect(1500 * self.scale_factor, 200 * self.scale_factor, self.button_width * self.scale_factor, self.button_height * self.scale_factor)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # Check if mouse click is within the checkboxes' area
                    for i, mode in enumerate(["301", "501", "Cricket"]):
                        checkbox_x = 100 * self.scale_factor + (self.checkbox_size + 10) * self.scale_factor
                        checkbox_y = (350 + i * (self.label_font_size + self.spacing)) * self.scale_factor
                        if checkbox_x <= mouse_x <= checkbox_x + self.checkbox_size * self.scale_factor and \
                                checkbox_y <= mouse_y <= checkbox_y + self.checkbox_size * self.scale_factor:
                            self.selected_game_mode = mode
                            print("Selected mode:", mode)  # For debugging purposes

                    # Check if mouse click is within the text fields' area
                    for i in range(len(self.text_fields)):
                        text_field_x = 525 * self.scale_factor
                        text_field_y = (50 + i * (self.label_font_size + self.spacing)) * self.scale_factor
                        text_field_width = 200 * self.scale_factor
                        text_field_height = self.label_font_size * self.scale_factor
                        if text_field_x <= mouse_x <= text_field_x + text_field_width and \
                                text_field_y <= mouse_y <= text_field_y + text_field_height:
                            self.active_text_field = i

                    # Check if mouse click is within the buttons' area
                    if self.start_button_rect.collidepoint(mouse_x, mouse_y):
                        print("Start button clicked")
                        # Add your start game logic here

                    if self.reset_button_rect.collidepoint(mouse_x, mouse_y):
                        print("Reset button clicked")
                        # Add your reset game logic here

                elif event.type == KEYDOWN:
                    if self.active_text_field is not None:
                        if event.key == K_BACKSPACE:
                            self.text_fields[self.active_text_field] = self.text_fields[self.active_text_field][:-1]
                        else:
                            self.text_fields[self.active_text_field] += event.unicode

            self.screen.fill((110, 150, 150))

            # Draw the label for checkboxes
            label = self.font.render("Select Game Mode", True, (0, 0, 0))
            label_rect = label.get_rect(topleft=(100 * self.scale_factor, 300 * self.scale_factor))  # Adjusted position based on scale factor
            self.screen.blit(label, label_rect)

            # Draw the game mode texts and checkboxes
            for i, (mode, text) in enumerate(zip(["301", "501", "Cricket"], ["301", "501", "Cricket"])):
                text_surface = self.font.render(text, True, (0, 0, 0))
                text_rect = text_surface.get_rect(topleft=(175 * self.scale_factor, (350 + i * (self.label_font_size + self.spacing)) * self.scale_factor))
                self.screen.blit(text_surface, text_rect)

                checkbox_x = 100 * self.scale_factor + (self.checkbox_size + 10) * self.scale_factor
                checkbox_y = (350 + i * (self.label_font_size + self.spacing)) * self.scale_factor
                self.draw_checkbox(self.screen, checkbox_x, checkbox_y, self.selected_game_mode == mode)

            # Draw the numbered text fields
            for i, text_field in enumerate(self.text_fields):
                text_field_label = self.font.render(f"#{i + 1}", True, (0, 0, 0))  # Corrected indexing
                text_field_label_rect = text_field_label.get_rect(topleft=(450 * self.scale_factor, (50 + i * (self.label_font_size + self.spacing)) * self.scale_factor))
                self.screen.blit(text_field_label, text_field_label_rect)

                # Draw text field rectangle
                pygame.draw.rect(self.screen, (0, 0, 0), (525 * self.scale_factor, (50 + i * (self.label_font_size + self.spacing)) * self.scale_factor, 200 * self.scale_factor, self.label_font_size * self.scale_factor), 2)

                # Draw the label for text fields
                label_text = self.font.render("Team/Player", True, (0, 0, 0))
                label_text_rect = label_text.get_rect(topleft=(480 * self.scale_factor, 0 * self.scale_factor))  # Adjusted position based on scale factor
                self.screen.blit(label_text, label_text_rect)

                # Highlight active text field
                if self.active_text_field == i:
                    pygame.draw.rect(self.screen, (255, 255, 255), (525 * self.scale_factor, (50 + i * (self.label_font_size + self.spacing)) * self.scale_factor, 200 * self.scale_factor, self.label_font_size * self.scale_factor), 2)

            # Draw buttons with beveled appearance
            pygame.draw.rect(self.screen, (100, 100, 100), self.start_button_rect)
            pygame.draw.rect(self.screen, (140, 140, 140), self.start_button_rect.inflate(-3, -3))
            pygame.draw.rect(self.screen,  (100, 100, 100), self.reset_button_rect)
            pygame.draw.rect(self.screen, (140, 140, 140), self.reset_button_rect.inflate(-3, -3))

            pygame.display.flip()
            self.clock.tick(60)

            # Handle window resizing
            if event.type == VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                self.update_layout()

if __name__ == "__main__":
    pygame.init()
    mainScreen = MainScreen()
    mainScreen.run()
