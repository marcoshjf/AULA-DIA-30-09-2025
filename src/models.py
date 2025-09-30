from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

@dataclass
class User:
    id: int
    name: str
    email: str
    active: bool = True

    def __post_init__(self):
        if not self.name or not self.name.strip():
            raise ValueError("Nome inválido.")
        if not EMAIL_RE.match(self.email):
            raise ValueError("Email inválido.")


@dataclass
class UserList:
    items: List[User] = field(default_factory=list)

    def next_id(self) -> int:
        return (self.items[-1].id + 1) if self.items else 1
