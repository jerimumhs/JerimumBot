run:
	python run.py

config.env:
	cp .env.example .env

test:
	python -m unittest discover