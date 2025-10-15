# DEV:
dev:
	docker-compose -f docker-compose.dev.yml up --build

dev-down:
	docker-compose -f docker-compose.dev.yml down -v

# TEST: (pytest)
test:
	docker-compose -f docker-compose.test.yml up --build --abort-on-container-exit
	docker-compose -f docker-compose.test.yml down -v

# PROD:
prod:
	docker-compose -f docker-compose.prod.yml up --build -d

prod-down:
	docker-compose -f docker-compose.prod.yml down -v

# Limpeza geral (remove tudo)
clean:
	docker system prune -f
	docker volume prune -f
