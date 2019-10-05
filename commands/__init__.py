from commands.base import config_handlers as base_handler
from core import BotTelegramCore


handlers = [
    base_handler
]


def config_handlers(instance: BotTelegramCore):
    for handler in handlers:
        handler(instance)
