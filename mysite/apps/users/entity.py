from apps.sql_app.entity import Entity
from dataclasses import dataclass, field

@dataclass(eq=False, slots=True)
class User(Entity):
    email: str
    hash_passsword: str
    is_active: bool
