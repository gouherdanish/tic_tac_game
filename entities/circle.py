from entities.special_entity import SpecialEntity
from entities.entity_type import EntityType

class Circle(SpecialEntity):
    def __init__(self,entity_type) -> None:
        super().__init__()
        self.entity_type = EntityType.CIRCLE