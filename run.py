import logging

from decouple import config

from app import app
from bot import JerimumBot


if __name__ == '__main__':
    bot = JerimumBot(token=config('BOT_TOKEN', default='??'))

    bot.run()
    app.run(host='0.0.0.0', port=config('PORT', default=8443, cast=int))
