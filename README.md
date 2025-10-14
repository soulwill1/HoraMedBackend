💊 HoraMed - Backend

API do sistema HoraMed, responsável por gerenciar usuários, medicamentos e notificações.

Desenvolvido em Python, com foco em simplicidade, escalabilidade e boas práticas.

🚀 Funcionalidades

    Cadastro e gerenciamento de usuários.

    Cadastro de medicamentos e horários.

    Geração de lembretes e notificações.

    API para integração com o frontend (Next.js).

🛠️ Tecnologias

    Python 3.11

    FastAPI para o desenvolvimento da API.

    PostgreSQL como banco de dados principal.

    Docker & Docker Compose para orquestração de ambiente.

📦 Configuração e Execução (Recomendado: Docker Compose)

A maneira mais fácil e recomendada de rodar o projeto é utilizando o Docker Compose, garantindo que o ambiente da aplicação e o banco de dados estejam configurados corretamente.

1. Pré-requisitos

Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.

2. Arquivos de Ambiente (.env)

O projeto utiliza variáveis de ambiente para a configuração. Crie um arquivo chamado .env_dev na raiz do projeto, baseado em um modelo (se houver), ou com as seguintes variáveis de exemplo:

# .env_dev
POSTGRES_USER=horamed_user
POSTGRES_PASSWORD=horamed_password
POSTGRES_DB=horamed_dev
ENV=dev

3. Comandos de Execução

Modo Desenvolvimento (DEV)

Use este modo para rodar a API com recarregamento automático (--reload).
Bash

# Define o ambiente DEV e sobe os containers (API + Banco de Dados)
ENV=dev docker-compose up --build

Após o banco de dados estar pronto, a API estará acessível em http://localhost:8000.

Modo Produção (PROD)

Use este modo para rodar a aplicação com Gunicorn e UvicornWorker de forma performática.
Bash

# Define o ambiente PROD e sobe os containers em modo detached (-d)
ENV=prod docker-compose up --build -d

Para ver os logs: docker-compose logs -f horamed

Rodar Testes

O ambiente de testes é configurado para executar o pytest e fechar o container logo em seguida.
Bash

# Define o ambiente TEST, sobe o banco de dados e executa os testes
ENV=test docker-compose run --rm horamed

💻 Configuração Local (Método Alternativo)

Se preferir rodar a aplicação diretamente na sua máquina:

    Clone o repositório:
    Bash

git clone https://github.com/soulwill1/HoraMed.git
cd HoraMed/HoraMed-backend

Crie e Ative o Ambiente Virtual:
Bash

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Instale as Dependências:
Bash

pip install -r requirements.txt

Execute o Servidor (Conecte a um DB local):
Bash

# Certifique-se de que seu banco de dados PostgreSQL está rodando
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

(Você precisará configurar as variáveis de ambiente do seu DB local manualmente.)
