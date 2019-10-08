run:
	python run.py

test:
	python -m unittest discover

flake8:
	flake8

config.env:
	cp .env.example .env

pip.install:
	pip install -r requirements.txt

heroku.purge_cache:
	heroku repo:purge_cache -a jerimumhsbot
