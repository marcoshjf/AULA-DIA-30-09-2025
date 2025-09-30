from __future__ import annotations
import types
from src.services import UserService
from src.models import User

class DummyRepo:
    def __init__(self):
        self.data = []

    def add(self, user: User) -> None:
        self.data.append(user)

    def list_all(self):
        return list(self.data)

    def find_by_id(self, user_id: int):
        return next((u for u in self.data if u.id == user_id), None)

    def save(self): pass

class DummyEmailer:
    def __init__(self):
        self.sent = []

    def send_welcome(self, name: str, email: str):
        self.sent.append((name, email))

class DummyApi:
    def __init__(self, payload=None):
        self.payload = payload or {"name": "Leanne Graham", "email": "Sincere@april.biz"}
    def get_user(self, user_id: int):
        return self.payload if user_id == 1 else None

def test_add_user_sends_email_and_persists():
    service = UserService(DummyRepo(), DummyEmailer(), DummyApi())
    user = service.add_user("Ana", "ana@example.com")

    assert user.id == 1
    assert user.name == "Ana"
    assert user.email == "ana@example.com"
    assert service.list_users()[0].name == "Ana"

def test_deactivate_user():
    repo = DummyRepo()
    emailer = DummyEmailer()
    api = DummyApi()
    service = UserService(repo, emailer, api)
    u = service.add_user("Bob", "bob@example.com")
    ok = service.deactivate_user(u.id)
    assert ok is True
    assert repo.find_by_id(u.id).active is False

def test_fetch_user_from_api():
    service = UserService(DummyRepo(), DummyEmailer(), DummyApi())
    data = service.fetch_user_from_api(1)
    assert data["email"] == "Sincere@april.biz"
    assert service.fetch_user_from_api(999) is None
