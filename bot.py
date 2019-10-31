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

    _chat_id = config('JERIMUM_CHAT_ID', default=-1001088768449, cast=int)

    def __init__(self):
        super(JerimumBot, self).__init__()
        self._handlers_configured = False
        self.config_handlers()

    def config_handlers(self):
        for config_handler in handlers:
            config_handler(self)
        self._handlers_configured = True

    @property
    def chat_id(self):
        return self._chat_id

    @classmethod
    def send_message(cls, text, chat_id=None, parse_mode=None):
        super().send_message(text, chat_id or cls._chat_id, parse_mode)


if __name__ == '__main__':
    JerimumBot.instance().run()
