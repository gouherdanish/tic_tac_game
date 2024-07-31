from entities.cell import Cell

class Game:

    def __init__(self,grid) -> None:
        self.grid = grid
        self.players = []
    
    def add_player(self,player):
        self.players.append(player)

    def has_won(self,player):

    
    def start(self):
        """
        Cross Player starts the game and then both players play alternately
        First player who makes a sequence horizontally, vertically or diagonally, wins
        """
        while True:
            for player in self.players:
                entity = player.get_entity()
                row, col = input(f"Hey {player.name}, where to put '{entity}'?").split()
                self.grid[row,col] = Cell(row,col,entity)
                if self.has_won(player):
                    print(f'{player.name} Won')
                    break