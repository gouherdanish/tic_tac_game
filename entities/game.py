class Game:
    def __init__(self,board,players) -> None:
        self.board = board
        self.players = players
        self.numof_active_players = 0

    def is_over(self):
        return self.numof_active_players < 2
    
    def start(self):
        pass