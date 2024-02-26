class Stats():
    """Tracking stats"""

    def __init__(self):
        """Initialization stats"""
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """Changing stats"""
        self.ships_left = 1
        self.score = 0

        