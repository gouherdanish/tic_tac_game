from entities.cell import Cell

class Game:
    def __init__(self,grid) -> None:
        self.grid = grid
        self.players = []
        self.is_over_flag = False
    
    def add_player(self,player):
        """
        Function to add a new player to the current game

        @param: player
        """
        self.players.append(player)

    def is_over(self):
        """
        Function to flag if the game is over
        """
        return self.is_over_flag

    def has_won(self,player):
        """
        Function to check if given player has won
        e.g. there are 8 ways a player can win in a 3*3 grid
        - 3 horizontal
        - 3 vertical
        - 2 diagonal

        @param: player
        """
        for j in range(self.grid.ncols):
            c1 = all(self.grid.get(i,j) == player.entity for i in range(self.grid.nrows))   # Vertical check at j
            c2 = all(self.grid.get(j,i) == player.entity for i in range(self.grid.nrows))   # Horizontal check at j
            if c1 or c2: return True
        c3 = all(self.grid.get(k,k) == player.entity for k in range(self.grid.ncols))       # Diagonal check 1
        c4 = all(self.grid.get(2-k,k) == player.entity for k in range(self.grid.ncols))     # Diagonal check 2
        if c3 or c4: return True
        return False
    
    def start(self):
        """
        Simulates the Game play

        Cross Player starts the game and then both players play alternately
        First player who makes a sequence horizontally, vertically or diagonally, wins
        """
        while not self.is_over():
            for player in self.players:
                entity = player.get_entity()
                self.grid.show()
                row, col = map(int,input(f"Hey {player.name}, where to put '{entity}' ? ").split(' '))
                self.grid.set(row,col,entity)
                if self.has_won(player):
                    print(f'{player.name} Won')
                    self.grid.show()
                    self.is_over_flag = True
                    break