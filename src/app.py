from __future__ import annotations
from .repository import InMemoryUserRepository
from .emailer import FileLogEmailer
from .api import UserApiClient
from .services import UserService
from .menu import menu_loop

def main() -> None:
    repo = InMemoryUserRepository()
    emailer = FileLogEmailer("log_email.txt")
    api = UserApiClient()
    service = UserService(repo, emailer, api)
    menu_loop(service)

if __name__ == "__main__":
    main()
