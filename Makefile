run:
	python bot.py

deploy.heroku:
	git push heroku feature/bot_class:master
