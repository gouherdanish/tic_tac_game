
class Player:
    def __init__(self,name:str,entity:str) -> None:
        self.name = name
        self.entity = entity

    def __str__(self) -> str:
        return f'{self.name}'

    def set_entity(self,entity):
        self.entity = entity

    def get_entity(self):
        return self.entity
