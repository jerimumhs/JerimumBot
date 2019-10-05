run:
	python run.py

test:
	python -m unittest discover

config.env:
	cp .env.example .env