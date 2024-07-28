from entities.special_entity import SpecialEntity

class Cell:
    def __init__(self,row,col) -> None:
        self.row = row
        self.col = col
        self.value = None

    def __str__(self) -> str:
        return f'({self.row},{self.col})'
    
    def __repr__(self) -> str:
        return str(self)
    
    def set_value(self,val:SpecialEntity) -> None:
        self.value = val

    def get_value(self) -> SpecialEntity:
        return self.value