from core import BotTelegramCore
from mixins import (BaseCommandsBotMixin, CallbackBotMixin, ErrorBotMixin,
                    MessageBotMixin, StickerBotMixin)
from commands import config_handlers


class JerimumBot(CallbackBotMixin, ErrorBotMixin,
                 MessageBotMixin, StickerBotMixin):
    """Bot Controller"""

    def config_handlers(self):
        for BaseClass in self.__class__.__bases__:
            assert issubclass(BaseClass, BotTelegramCore)
            BaseClass.config_handlers(self)
        config_handlers(self)
