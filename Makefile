run:
	python run.py

test:
	python -m unittest discover tests

config.env:
	cp .env.example .env

pip.install:
	pip install -r requirements.txt