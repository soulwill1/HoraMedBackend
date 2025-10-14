💊 HoraMed - Backend

API do sistema HoraMed, responsável por gerenciar usuários, medicamentos e notificações.

Desenvolvido em Python, com foco em simplicidade, escalabilidade e boas práticas.

Funcionalidades

    Cadastro e gerenciamento de usuários.

    Cadastro de medicamentos e horários.

    Geração de lembretes e notificações.

    API para integração com o frontend (Next.js).

Tecnologias

    Python 3.11

    FastAPI para o desenvolvimento da API.

    PostgreSQL como banco de dados principal.

    Docker & Docker Compose para orquestração de ambiente.

Configuração e Execução (Recomendado: Docker Compose)

A maneira mais fácil e recomendada de rodar o projeto é utilizando o Docker Compose, garantindo que o ambiente da aplicação e o banco de dados estejam configurados corretamente.

1. Pré-requisitos

Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.

2. Arquivos de Ambiente (.env)

O projeto exige que as variáveis de configuração do ambiente (ENV, ENV_FILE, ENV_VOLUME) e do banco de dados sejam definidas.

Crie o arquivo .env_dev na raiz do projeto com as seguintes variáveis:
Ini, TOML

# .env_dev

# Variáveis do Banco de Dados
POSTGRES_USER=horamed_user
POSTGRES_PASSWORD=horamed_password
POSTGRES_DB=horamed_dev

# Variáveis de Configuração do Docker Compose (Obrigatórias)
# Estas variáveis são lidas pelo docker-compose.yml para carregar o env_file e o volume
ENV=dev
ENV_FILE=.env_dev
ENV_VOLUME=./app_data_dev:/app/data

O valor de ENV_VOLUME define um volume local (./app_data_dev) para persistência de dados do container.

3. Comandos de Execução

Usaremos a flag --env-file para carregar todas as variáveis necessárias de forma limpa.

Modo Desenvolvimento (DEV)

Use este modo para rodar a API com recarregamento automático (--reload).
Bash

# Sobe os containers, carregando todas as variáveis de .env_dev
docker-compose --env-file .env_dev up --build

Após o banco de dados estar pronto, a API estará acessível em http://localhost:8000.

Modo Produção (PROD)

Crie um arquivo .env_prod e use este modo para rodar a aplicação com Gunicorn e UvicornWorker.
Bash

# Sobe os containers em modo detached (-d) usando o arquivo de PROD
docker-compose --env-file .env_prod up --build -d

Para ver os logs: docker-compose logs -f horamed

Rodar Testes

O ambiente de testes deve usar um arquivo de variáveis dedicado (e.g., .env_test) e executa o pytest como um comando one-off.
Bash

# Executa os testes e remove o container após o término
docker-compose --env-file .env_test run --rm horamed

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

# ATENÇÃO: Certifique-se de que seu banco de dados PostgreSQL está rodando localmente
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

(As variáveis de conexão com o banco de dados deverão ser exportadas para o seu shell manualmente antes de rodar o uvicorn.)
