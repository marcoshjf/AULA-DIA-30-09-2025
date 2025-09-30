
NOME DA EQUIPE:
MARCOS HENRIQUE JERONIMO FERNANDES
MATEUS ZANIN FERNANDES



# User Management (Refatoração focada em dependências)

Este projeto refatora um sistema simples de gerenciamento de usuários com os objetivos de:
- Reduzir acoplamento entre módulos (dependências internas)
- Melhorar a organização em camadas (domain/repository/services/interface)
- Tornar funções testáveis (injeção de dependências e funções com efeitos colaterais confinados)
- Incluir uma biblioteca externa gerenciada por *pip* (**httpx**) para chamadas HTTP

## O que mudou

### Antes
- Funções monolíticas misturando entrada de usuário, regras de negócio, I/O de arquivo e requisições HTTP.
- Forte acoplamento: `requests`, arquivo de log, `print` e `input` espalhados por todo o código.
- Difícil de testar (depende de I/O e rede).

### Depois
- **Camadas separadas**:
  - `models.py` – Entidades (`User`) e validações
  - `repository.py` – Repositório (in-memory) com protocolo (fácil trocar por arquivo/DB)
  - `emailer.py` – Serviço de e-mail (aqui simulado via log em arquivo)
  - `api.py` – Cliente HTTP externo usando **httpx** (biblioteca externa)
  - `services.py` – Regras de negócio e orquestração (sem `input/print`)
  - `menu.py` – Interface de console (apenas I/O)
  - `app.py` – *Composition root* (injeção de dependências)
- **Injeção de dependências**: repositório, emailer e cliente HTTP são passados para o `UserService`.
- **Testabilidade**: testes unitários com *fakes* (sem I/O real e sem rede).
- **Efeitos colaterais confinados**: apenas em `emailer.FileLogEmailer` e `menu.py`.

## Dependências

- `httpx` (runtime)
- `pytest` (dev/test)

Instalação (recomendado usar venv):

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
