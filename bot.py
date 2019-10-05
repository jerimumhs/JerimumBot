from core import BotTelegramCore
from commands import handlers


class JerimumBot(BotTelegramCore):
    """Bot Controller"""

    def config_handlers(self):
        for config_handler in handlers:
            config_handler(self)
