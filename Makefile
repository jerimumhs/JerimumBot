current_dir = $(notdir $(shell pwd))

config.env:
	cp .env.example .env

##############################
### LOCAL PYTHON COMMANDS ###
#############################
run:
	python run.py

test:
	pytest

flake8:
	flake8

pip.install:
	pip install -r requirements.txt

##############################
###### DOCKER COMMANDS ######
#############################
docker.build:
	docker-compose build

docker.logs:
	docker-compose logs -f

docker.up:
	docker-compose up -d

docker.down:
	docker-compose down

docker.bash:
	docker-compose run bot bash

docker.bot.stop:
	docker stop $(current_dir)_bot_1

docker.bot.restart: docker.bot.stop docker.up

docker.test:
	docker-compose run bot pytest

docker.flake8:
	docker-compose run bot flake8

##############################
###### HEROKU COMMANDS ######
#############################
heroku.prod.add_remote:
	heroku git:remote -a jerimumhsbot
	git remote rename heroku heroku-prod

heroku.prod.deploy:
	git push heroku-prod master

heroku.prod.purge_cache:
	heroku repo:purge_cache -a jerimumhsbot

heroku.dev.add_remote:
	heroku git:remote -a jerimumhstestbot
	git remote rename heroku heroku-dev

heroku.dev.deploy:
	git push heroku-dev dev:master

heroku.dev.purge_cache:
	heroku repo:purge_cache -a jerimumhstestbot