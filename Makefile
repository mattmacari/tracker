
build:
	docker-compose build -f docker-compose-build.yml

up:
	docker-compose up --build

deatched-up: 
	docker-compose up -d

down:
	docker-compose down

check:
	docker-compose run web python manage.py check

makemigrations:
	docker-compose run web python manage.py makemigrations

migrate:
	docker-compose run web python manage.py migrate