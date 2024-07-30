from entities.cross import Cross
from entities.circle import Circle
from entities.special_entity import SpecialEntity

class Player:
    def __init__(self,name:str) -> None:
        self.name = name
        self.cells = []
        self.entity = None

    def play(self,cell):
        self.cells.append(cell)

    def set_entity(self,entity):
        self.entity = entity

    def get_entity(self):
        return self.entity

    def has_won(self):
        pass


# class CrossPlayer(Player):
#     def __init__(self, name) -> None:
#         super().__init__(name)
    
#     def play(self,cell):
#         cell.value = Cross()

# class CirclePlayer(Player):
#     def __init__(self, name) -> None:
#         super().__init__(name)
    
    # def play(self,cell):
    #     cell.value = Circle()
    #     self.cells.append(cell)