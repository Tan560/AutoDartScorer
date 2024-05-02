import pygame
import sys
from pygame.locals import *

from gameMode import gameMode301, gameMode501, gameModeCricket

class MainScreen:
    def __init__(self):
        self.target_width = 1920
        self.target_height = 1080
        self.screen = pygame.display.set_mode((self.target_width, self.target_height), RESIZABLE)  # Initial resolution
        pygame.display.set_caption("Dart Scoring Game")

        self.scale_factor = 1.5  # Scale factor for resizing elements
        self.label_font_size = 36
        self.checkbox_size = 20
        self.spacing = 30

        self.font = pygame.font.Font(None, int(self.label_font_size * self.scale_factor))
        self.clock = pygame.time.Clock()

        self.text_fields = ["" for _ in range(10)]
        self.active_text_field = None

        mode = "301"
        self.selected_game_mode = gameMode301(self.text_fields)   # Set the selected game mode to "301"
        
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

    def handle_events(self):
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
                        if mode == "301":
                            self.selected_game_mode = gameMode301(self.text_fields)
                        elif mode == "501":
                            self.selected_game_mode = gameMode501(self.text_fields)
                        else:
                            self.selected_game_mode = gameModeCricket(self.text_fields)
                       
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
                    self.selected_game_mode.game_mode_screen()

                if self.reset_button_rect.collidepoint(mouse_x, mouse_y):
                    self.text_fields = ["" for _ in range(10)]

            elif event.type == KEYDOWN:
                if self.active_text_field is not None:
                    if event.key == K_BACKSPACE:
                        self.text_fields[self.active_text_field] = self.text_fields[self.active_text_field][:-1]
                    else:
                        self.text_fields[self.active_text_field] += event.unicode

            elif event.type == VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                self.update_layout()

    def draw(self):
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
            checked = isinstance(self.selected_game_mode, globals()[f"gameMode{mode}"])
            self.draw_checkbox(self.screen, checkbox_x, checkbox_y, checked)

        # Draw the numbered text fields
        for i, (text_field, label_text) in enumerate(zip(self.text_fields, [f"#{n+1}" for n in range(10)])):
            # Draw text field rectangle
            pygame.draw.rect(self.screen, (0, 0, 0), (525 * self.scale_factor, (50 + i * (self.label_font_size + self.spacing)) * self.scale_factor, 200 * self.scale_factor, self.label_font_size * self.scale_factor), 2)

            # Draw the label for text fields
            label_text_surface = self.font.render(label_text, True, (0, 0, 0))
            label_text_rect = label_text_surface.get_rect(topleft=(480 * self.scale_factor, (55 + i * (self.label_font_size + self.spacing)) * self.scale_factor))
            self.screen.blit(label_text_surface, label_text_rect)

            # Highlight active text field
            if self.active_text_field == i:
                pygame.draw.rect(self.screen, (255, 255, 255), (525 * self.scale_factor, (50 + i * (self.label_font_size + self.spacing)) * self.scale_factor, 200 * self.scale_factor, self.label_font_size * self.scale_factor), 2)

            # Render text in the text fields
            text_surface = self.font.render(text_field, True, (0, 0, 0))
            text_rect = text_surface.get_rect(topleft=((525 + 5) * self.scale_factor, (60 + i * (self.label_font_size + self.spacing)) * self.scale_factor))
            self.screen.blit(text_surface, text_rect)

        # Draw buttons with beveled appearance
        start_button_color = (100, 100, 100)
        reset_button_color = (100, 100, 100)
        
        if self.start_button_rect.collidepoint(pygame.mouse.get_pos()):
            start_button_color = (50, 50, 50)  # Darker color when mouse hovers over start button
            if pygame.mouse.get_pressed()[0]:  # If left mouse button is pressed
                start_button_color = (140, 140, 140)  # Darker color when button is pressed
            
        if self.reset_button_rect.collidepoint(pygame.mouse.get_pos()):
            reset_button_color = (50, 50, 50)  # Darker color when mouse hovers over reset button
            if pygame.mouse.get_pressed()[0]:  # If left mouse button is pressed
                reset_button_color = (140, 140, 140)  # Darker color when button is pressed
        
        pygame.draw.rect(self.screen, start_button_color, self.start_button_rect)
        pygame.draw.rect(self.screen, (140, 140, 140), self.start_button_rect.inflate(-3, -3))
        start_text = self.font.render("Start", True, (255, 255, 255))
        start_text_rect = start_text.get_rect(center=self.start_button_rect.center)
        self.screen.blit(start_text, start_text_rect)

        pygame.draw.rect(self.screen,  reset_button_color, self.reset_button_rect)
        pygame.draw.rect(self.screen, (140, 140, 140), self.reset_button_rect.inflate(-3, -3))
        reset_text = self.font.render("Reset", True, (255, 255, 255))
        reset_text_rect = reset_text.get_rect(center=self.reset_button_rect.center)
        self.screen.blit(reset_text, reset_text_rect)

        pygame.display.flip()


    def run(self):
        while True:
            self.handle_events()
            self.draw()
            self.clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    mainScreen = MainScreen()
    mainScreen.run()
