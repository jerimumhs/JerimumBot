import logging

from decouple import config

from bot import JerimumBot


if __name__ == '__main__':
    instance = JerimumBot.instance()

    try:
        mode = config('MODE', default='cmd')
        if mode == 'cmd':
            instance.run_cmd()
        elif mode == 'web':
            instance.run_web()
        else:
            raise Exception('O modo passado não foi reconhecido')

    except Exception as e:
        logging.error(f'Modo: {config("MODE", default="cmd")}')
        logging.error(f'token: {instance.token}')
        logging.error(f'Port: {instance.port}')
        logging.error(f'heroku app name: {instance.server_url}')
        raise e
