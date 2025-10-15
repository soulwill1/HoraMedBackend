FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

COPY app ./app
COPY tests ./tests
COPY scripts/wait-for-postgres.sh ./wait-for-postgres.sh
RUN chmod +x ./wait-for-postgres.sh

ARG ENV=prod
ENV ENV=${ENV}

EXPOSE 8000

CMD ["sh", "wait-for-postgres.sh", "db"]

