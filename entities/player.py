from entities.cross import Cross
from entities.circle import Circle


class Player:
    def __init__(self,name) -> None:
        self.name = name
        self.cells = []


class CrossPlayer(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def play(self,cell):
        cell.value = Cross()

class CirclePlayer(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def play(self,cell):
        cell.value = Circle()
        self.cells.append(cell)