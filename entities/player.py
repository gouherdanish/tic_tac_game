
class Player:
    def __init__(self,name:str,entity:str) -> None:
        self.name = name
        self.entity = entity

    def set_entity(self,entity):
        self.entity = entity

    def get_entity(self):
        return self.entity


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