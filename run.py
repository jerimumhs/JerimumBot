import logging

from decouple import config

from bot import JerimumBot

if __name__ == '__main__':
    instance = JerimumBot(
        token=config('BOT_TOKEN', default='??'),
        port=config('PORT', default=8443, cast=int),
        heroku_app_name=config('HEROKU_APP_NAME', default='??')
    )
    try:
        instance.run(config('MODE', default='cmd'))
    except Exception as e:
        logging.error(f'Modo: {config("MODE", default="cmd")}')
        logging.error(f'token: {instance.token}')
        logging.error(f'Port: {instance.port}')
        logging.error(f'heroku app name: {instance.heroku_app_name}')
        raise e