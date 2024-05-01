class gameMode:
    def __init__(self):
        pass

    def calculate_score(self, dart_position):
        pass
    def game_mode_screen(self):
        pass
    # Add other game mode-related methods here

class gameMode301(gameMode):
    def __init__(self):
        super().__init__()
        # Implement 301 game mode-specific logic here

    def calculate_score(self, dart_position):
        return super().calculate_score(dart_position)

    def game_mode_screen(self):
        print("Works")
        return super().game_mode_screen()

class gameMode501(gameMode):
    def __init__(self):
        super().__init__()
        # Implement 501 game mode-specific logic here
    
    def calculate_score(self, dart_position):
        return super().calculate_score(dart_position)

    def game_mode_screen(self):
        return super().game_mode_screen()

class gameModeCricket(gameMode):
    def __init__(self):
        super().__init__()
        # Implement Cricket game mode-specific logic here

    def calculate_score(self, dart_position):
        return super().calculate_score(dart_position)

    def game_mode_screen(self):
        return super().game_mode_screen()