class Game:

    def __init__(self,board) -> None:
        self.board = board
        self.players = []
        self.numof_active_players = 0

    def is_over(self):
        return self.numof_active_players < len(self.players)
    
    def add_player(self,player):
        self.players.append(player)
        self.numof_active_players += 1
    
    def start(self):
        """
        Cross Player starts the game and then both players play alternately
        First player who makes a sequence horizontally, vertically or diagonally, wins
        """
        while not self.is_over():
            pass