
### 📂 `HoraMed-backend/README.md`
```markdown
# HoraMed - Backend

API do sistema HoraMed, responsável por gerenciar usuários, medicamentos e notificações.  
Desenvolvido em **Python**, com foco em simplicidade, escalabilidade e boas práticas.

## 🚀 Funcionalidades
- Cadastro e gerenciamento de usuários.
- Cadastro de medicamentos e horários.
- Geração de lembretes e notificações.
- API para integração com o frontend (Next.js).

## 🛠️ Tecnologias
- [Python 3.x](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) (ou Flask, dependendo da escolha)
- [SQLAlchemy](https://www.sqlalchemy.org/) + SQLite/PostgreSQL
- [Alembic](https://alembic.sqlalchemy.org/) para migrações de banco de dados

## 📦 Instalação
```bash
# Clone o repositório
git clone https://github.com/soulwill1/HoraMed.git
cd HoraMed/HoraMed-backend

# Crie o ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute o servidor
uvicorn app.main:app --reload
