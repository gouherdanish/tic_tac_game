from entities.cell import Cell

class Grid:
    def __init__(self,nrows,ncols) -> None:
        self.nrows = nrows
        self.ncols = ncols
        self.arr = [['-' for i in range(nrows)] for j in range(ncols)]

    def __str__(self) -> str:
        return f'{self.arr}'
    
    def set(self,row,col,entity):
        self.arr[row][col] = entity
    
    def get(self,row,col):
        return self.arr[row][col]
    
    def show(self):
        for i in range(self.nrows):
            print('|'.join(self.arr[i]))
            if i == self.nrows - 1: break
            else: print('-'*5) 
