from time import sleep
from abc import ABC, abstractmethod
import logging

from telegram.ext import Updater, Handler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


class BotTelegramCore(ABC):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, token, port, server_url):
        logging.info('Inicializando o bot...')
        self.token = token
        self.port = port
        self.server_url = server_url

        self.__updater = Updater(self.token)
        self.config_handlers()

    @classmethod
    def send_message(cls, chat_id, text, parse_mode=None):
        instance = cls.instance()
        assert isinstance(instance, BotTelegramCore)
        instance.__updater.bot.send_message(chat_id=chat_id, text=text, parse_mode=parse_mode)

    @classmethod
    def instance(cls):
        while cls.__instance is None:
            logging.info('Esperando bot ser inicializado...')
            sleep(1)
        return cls.__instance

    @abstractmethod
    def config_handlers(self):
        raise NotImplementedError('Cannot call config_handler from BotCore')

    def add_handler(self, handler: Handler):
        if not isinstance(handler, Handler):
            raise ValueError("Handler deve ser do tipo Handler!")
        self.__updater.dispatcher.add_handler(handler)

    def add_error_handler(self, handler):
        self.__updater.dispatcher.add_error_handler(handler)

    def run_web(self):
        """Start the bot as a webhook server"""

        self.__updater.start_webhook(
            listen="0.0.0.0",
            port=self.port,
            url_path=self.token
        )

        self.__updater.bot.set_webhook(f"{self.server_url}/{self.token}")

        logging.info('Bot está rodando como um webserver!')
        # self.updater.idle()

    def run_cmd(self):
        """Start the bot as a python script loop"""
        self.__updater.start_polling()

        logging.info('Bot está rodando como um script python!')
        # self.updater.idle()
