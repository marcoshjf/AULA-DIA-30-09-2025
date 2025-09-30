from __future__ import annotations
from typing import Protocol, List, Optional
from .models import User, UserList

class UserRepository(Protocol):
    def add(self, user: User) -> None: ...
    def list_all(self) -> List[User]: ...
    def find_by_id(self, user_id: int) -> Optional[User]: ...
    def save(self) -> None: ...

class InMemoryUserRepository:
    """Repositório em memória; facilmente trocável por arquivo/DB depois."""
    def __init__(self) -> None:
        self._users = UserList()

    def add(self, user: User) -> None:
        self._users.items.append(user)

    def list_all(self) -> List[User]:
        return list(self._users.items)

    def find_by_id(self, user_id: int) -> Optional[User]:
        return next((u for u in self._users.items if u.id == user_id), None)

    def save(self) -> None:
        # no-op para memória; poderia persistir em arquivo/DB aqui
        pass
