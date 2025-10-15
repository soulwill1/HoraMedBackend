# Etapa 1: desenvolvimento (com hot reload e pytest)
FROM python:3.11-slim AS dev

WORKDIR /app

COPY requirements.txt ./
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir uvicorn pytest debugpy

COPY . .
COPY scripts/wait-for-postgres.sh ./scripts/wait-for-postgres.sh
RUN chmod +x scripts/wait-for-postgres.sh

CMD ["sh", "./scripts/wait-for-postgres.sh", "db"]


# Etapa 2: produção (mínima e otimizada)
FROM python:3.11-slim AS prod

WORKDIR /app

COPY requirements.txt ./
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY scripts/wait-for-postgres.sh ./wait-for-postgres.sh
RUN chmod +x ./wait-for-postgres.sh

EXPOSE 8000

CMD ["sh", "wait-for-postgres.sh", "db"]

# Etapa 3: testes

FROM dev AS test
CMD ["pytest", "-v"]