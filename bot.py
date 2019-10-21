import logging

from decouple import config

from core import BotTelegramCore
from commands import handlers


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


class JerimumBot(BotTelegramCore):
    """Bot Controller"""

    def config_handlers(self):
        for config_handler in handlers:
            config_handler(self)

    @classmethod
    def instance(cls):
        if super().instance() is None:
            return cls(token=config('BOT_TOKEN', default='??'))
        return super().instance()

    @classmethod
    def run(cls):
        super(cls, cls.instance()).run()


if __name__ == '__main__':
    JerimumBot.run()
