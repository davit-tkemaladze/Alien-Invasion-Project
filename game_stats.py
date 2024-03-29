class GameStats:
    """Track statistic for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.ship_limit = ai_game.settings.ship_limit
        self.reset_stats()

        # High score should never be reset.
        self.high_score = 0

        # Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ship_limit
        self.score = 0
        self.level = 1