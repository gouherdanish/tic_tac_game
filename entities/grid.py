class Grid:
    def __init__(self,nrows,ncols) -> None:
        self.nrows = nrows
        self.ncols = ncols
        self.arr = [['-' for i in range(nrows)] for j in range(ncols)]

    def __str__(self) -> str:
        return f'{self.arr}'
    
    def is_empty(self,row,col):
        if self.arr[row][col] == '-':
            return True
        else:
            print(f'The cell ({row},{col}) is already filled')
            return False
        
    def is_valid(self,row,col):
        if 0 <= row < self.nrows and 0 <= col < self.ncols:
            return True
        else:
            print(f'The cell ({row},{col}) is out of bounds')
            return False

    def set(self,row,col,entity):
        """
        Set entity value at (row,col) position in the current grid

        @param: row integer
        @param: col integer
        @param: entity
        """
        self.arr[row][col] = entity
    
    def get(self,row,col):
        """
        Return entity value present at (row,col) position in the current grid
        
        @param: row integer
        @param: col integer
        """
        return self.arr[row][col]
    
    def show(self):
        """
        Prints the Grid
        """
        for i in range(self.nrows):
            print('|'.join(self.arr[i]))
            if i == self.nrows - 1: break
            else: print('-'*5) 
