from __future__ import annotations
from typing import List, Optional
from .models import User
from .repository import UserRepository
from .emailer import Emailer
from .api import UserApiClient

class UserService:
    """
    Camada de orquestração. Sem I/O de console aqui.
    Recebe dependências por injeção, reduzindo acoplamento.
    """
    def __init__(self, repo: UserRepository, emailer: Emailer, api: UserApiClient):
        self.repo = repo
        self.emailer = emailer
        self.api = api

    # Funções puras ou com efeitos colaterais confinados
    def add_user(self, name: str, email: str) -> User:
        new_id = self._next_id()
        user = User(id=new_id, name=name.strip(), email=email.strip())
        self.repo.add(user)
        self.repo.save()
        # efeito colateral isolado no serviço de email (injeção)
        self.emailer.send_welcome(user.name, user.email)
        return user

    def list_users(self) -> List[User]:
        return self.repo.list_all()

    def deactivate_user(self, user_id: int) -> bool:
        user = self.repo.find_by_id(user_id)
        if not user:
            return False
        user.active = False
        self.repo.save()
        return True

    def fetch_user_from_api(self, user_id: int) -> Optional[dict]:
        if user_id <= 0:
            raise ValueError("user_id deve ser positivo.")
        return self.api.get_user(user_id)

    def _next_id(self) -> int:
        users = self.repo.list_all()
        return (users[-1].id + 1) if users else 1
