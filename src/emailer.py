from __future__ import annotations
from typing import Protocol
from datetime import datetime
from pathlib import Path

class Emailer(Protocol):
    def send_welcome(self, name: str, email: str) -> None: ...

class FileLogEmailer:
    """
    Implementação simples que 'envia' email escrevendo em log.
    Sem dependências externas; efeito colateral isolado.
    """
    def __init__(self, log_path: str = "log_email.txt") -> None:
        self.log_path = Path(log_path)

    def send_welcome(self, name: str, email: str) -> None:
        message = f"Olá {name}, bem-vindo ao sistema!"
        print(f"[EMAIL SIMULADO] Enviando para {email}: {message}")
        with self.log_path.open("a", encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat()} - {email} - {message}\n")
