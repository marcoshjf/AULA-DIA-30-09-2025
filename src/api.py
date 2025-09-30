from __future__ import annotations
import httpx

class UserApiClient:
    """
    Cliente API externo usando httpx (dependência externa).
    Injetável e com timeout configurado para testabilidade.
    """
    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com", timeout: float = 5.0):
        self.base_url = base_url
        self._client = httpx.Client(timeout=timeout)

    def get_user(self, user_id: int) -> dict | None:
        resp = self._client.get(f"{self.base_url}/users/{user_id}")
        if resp.status_code == 200:
            return resp.json()
        return None

    def close(self) -> None:
        self._client.close()

    def __del__(self):
        # garantia extra de fechamento
        try:
            self._client.close()
        except Exception:
            pass
