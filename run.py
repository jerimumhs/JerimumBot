from decouple import config

from app import app
from bot import JerimumBot


if __name__ == '__main__':
    JerimumBot.run()

    app.run(host='0.0.0.0', port=config('PORT', default=5000, cast=int))
