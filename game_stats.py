from highscoredata import HighScore
class GameStats:
    """Track the stats for the game"""
    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.highscore = HighScore()
        self.reset_stats()
        # Start Alien Invasion in an inctive state.
        self.game_active = False

        # High score should never reset
        self.high_score = self.highscore.pull_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1