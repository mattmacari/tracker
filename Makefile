
build:
	docker-compose build -f docker-compose-build.yml

up: 
	docker-compose up -d

down:
	docker-compose down