#!/bin/sh
set -e

if [ "$ENV" != "test" ]; then
  # Recebe o host do banco
  host="$1"
  echo "Aguardando o banco de dados em $host..."
  until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$host" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q' 2>/dev/null; do
    echo "Banco ainda não está pronto. Tentando novamente em 2s..."
    sleep 2
  done
  echo "Banco pronto!"
fi

# Decide o que rodar baseado no ENV
case "$ENV" in
  dev)
    echo "Rodando em modo DEV..."
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ;;
  test)
    echo "Rodando TESTES..."
    pytest -v
    ;;
  prod)
    echo "Rodando em modo PROD..."
    gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000
    ;;
  *)
    echo "ENV não definido ou inválido! Usando PROD como padrão."
    gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000
    ;;
esac
