from entities.special_entity import SpecialEntity
from entities.entity_type import EntityType

class Cross(SpecialEntity):
    def __init__(self) -> None:
        super().__init__()
        self.entity_type = EntityType.CROSS