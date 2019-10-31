from commands.base import config_handlers as base_handler
from commands.callback import config_handlers as callback_handler
from commands.error import config_handlers as error_handler
from commands.message import config_handlers as message_handler
from commands.sticker import config_handlers as sticker_handler
from commands.coach import config_handlers as coach_handler
from commands.weather import config_handlers as weather_handler
from commands.house import config_handlers as house_handler

handlers = [
    base_handler,
    callback_handler,
    error_handler,
    message_handler,
    sticker_handler,
    coach_handler,
    weather_handler,
    house_handler
]
