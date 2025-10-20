# HoraMed - Backend

API do sistema HoraMed, responsável por gerenciar usuários, medicamentos e notificações.  
Desenvolvido em **Python**, com foco em simplicidade, escalabilidade e boas práticas.

---

## Funcionalidades

- Cadastro e gerenciamento de usuários  
- Cadastro de medicamentos e horários  
- Geração de lembretes e notificações  
- API para integração com o frontend (Next.js)

---

## Tecnologias

- **Python 3.11**  
- **FastAPI** para desenvolvimento da API  
- **PostgreSQL** como banco de dados principal  
- **Docker** e **Docker Compose** para orquestração de ambiente

---

## Configuração e Execução

A execução do projeto é feita via **Makefile**.

### Comandos principais

```bash
make dev         # Sobe o ambiente de desenvolvimento
make dev-down    # Derruba o ambiente de desenvolvimento

make test        # Sobe o ambiente de testes
make test-down   # Derruba o ambiente de testes

make prod        # Sobe o ambiente de produção
make prod-down   # Derruba o ambiente de produção

make clean       # Remove containers e volumes

### Arquivos de Ambiente (.env)

Crie os arquivos .env_dev, .env_test e .env_prod conforme o ambiente desejado.
# Ambiente
- ENV=dev
- ENV_FILE=.env_dev
- ENV_VOLUME=./app_data_dev:/app/data

# Banco de dados
- POSTGRES_USER=user
- POSTGRES_PASSWORD=pass
- POSTGRES_DB=exemplodb
- DATABASE_URL=postgresql://user:pass@db:5432/exemplodb

# Segurança
- SECRET_KEY=senha
