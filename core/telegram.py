import logging
from abc import ABC, abstractmethod

from decouple import config
from telegram.ext import Updater, Handler
from telegram import Update


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


class BotTelegramCore(ABC):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            BotTelegramCore._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        logging.info('Inicializando o bot...')
        self.token = config('BOT_TOKEN')
        self.port = config('PORT', default=8443, cast=int)
        self.server_url = config('SERVER_URL')

        self._updater = Updater(self.token)
        self._running = False

    @classmethod
    def instance(cls):
        return cls._instance or cls()

    @abstractmethod
    def config_handlers(self):
        raise NotImplementedError(
            'Cannot call config_handler from BotTelegramCore'
        )

    @property
    @abstractmethod
    def chat_id(self):
        raise NotImplementedError(
            'Cannot call chat_id from BotTelegramCore'
        )

    @property
    def chat(self):
        return self._updater.bot.get_chat(self.chat_id)

    def is_from_oficial_chat(self, update: Update):
        return self.chat_id == update.message.chat.id

    @property
    def administrators(self):
        return [chat_member.user.id for
                chat_member in self.chat.get_administrators()]

    @classmethod
    def is_admin(cls, user_id):
        instance = cls.instance()
        return user_id in instance.administrators

    @classmethod
    def send_message(cls, text, chat_id, parse_mode=None):
        instance = cls.instance()
        instance._updater.bot.send_message(
            chat_id=chat_id,
            text=text,
            parse_mode=parse_mode
        )

    def add_handler(self, handler: Handler):
        if not isinstance(handler, Handler):
            raise ValueError("Handler deve ser do tipo Handler!")
        self._updater.dispatcher.add_handler(handler)

    def add_error_handler(self, handler):
        self._updater.dispatcher.add_error_handler(handler)

    def run_web(self):
        """Start the bot as a webhook server"""

        self._updater.start_webhook(
            listen="0.0.0.0",
            port=self.port,
            url_path=self.token
        )

        self._updater.bot.set_webhook(f"{self.server_url}/{self.token}")

        logging.info('Bot está rodando como um webserver!')
        self._updater.idle()

    def run_cmd(self):
        """Start the bot as a python script loop"""
        self._updater.start_polling()

        logging.info('Bot está rodando como um script python!')
        self._updater.idle()

    def run(self):
        """Start the bot as a python script loop"""
        if not self._running:
            self._updater.start_polling()

            logging.info('Bot está rodando como um script python!')
            self._running = True
        else:
            logging.info('Bot já está rodando!')
