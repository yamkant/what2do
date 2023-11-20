from project.domain.entity import Entity
from dataclasses import dataclass, field

@dataclass(eq=False, slots=True)
class User(Entity):
    email: str
    is_active: bool
