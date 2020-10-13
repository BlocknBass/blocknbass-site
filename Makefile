install-dev:
	 docker-compose build

install-prod:
	docker-compose -f docker-compose.prod.yml build
