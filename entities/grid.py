from entities.cell import Cell

class Grid:
    def __init__(self,nrows,ncols) -> None:
        self.nrows = nrows
        self.ncols = ncols
        self.arr = [[Cell(i,j).value for i in nrows] for j in range(ncols)]

    def __str__(self) -> str:
        return f'{self.arr}'
    
