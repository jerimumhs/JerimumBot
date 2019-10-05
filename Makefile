run:
	python run.py

test:
	python -m unittest discover

pip.install:
	pip install -r requirements.txt

config.env:
	cp .env.example .env