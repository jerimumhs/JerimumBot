import logging

import pyowm
from pyowm.exceptions.api_response_error import NotFoundError
from pyowm.exceptions.api_call_error import APICallError
from decouple import config
from telegram.ext import CommandHandler

from core import BotTelegramCore
from db import CommandCall
from messages import COMMAND_THROTTLED


logging.basicConfig(format='%(asctime)s - %(name)s - '
                           '%(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def weather(bot, update, args):
    """Define weather at certain location"""

    user = update.message.from_user
    bot_instance = BotTelegramCore.instance()

    if bot_instance.is_from_oficial_chat(update):
        if not CommandCall.allow_call(command=CommandCall.CLIMA):
            last_call = CommandCall.last_clima()
            bot.sendMessage(
                chat_id=user.id,
                text=COMMAND_THROTTLED.format(
                    segundos=last_call.cooldown_left,
                    comando=last_call.value))
            return

    api_key = config('OPENWEATHERMAP_TOKEN')
    owm = pyowm.OWM(api_key)
    text_location = " ".join(args)
    try:
        observation = owm.weather_at_place(text_location)
        _weather = observation.get_weather()
        humidity = _weather.get_humidity()
        wind = _weather.get_wind()
        temp = _weather.get_temperature('celsius')
        update.message.reply_text(f"🧭 Localização: {text_location}\n"
                                  f"🔥️ Temp. Maxima: "
                                  f"{temp.get('temp_max')} °C \n"
                                  f"❄️ Temp. Minima: "
                                  f"{temp.get('temp_min')} °C \n"
                                  f"💨 Vel. do Vento: "
                                  f"{wind.get('speed')} m/s \n"
                                  f"💧 Humidade: "
                                  f"{humidity}%")
        if bot_instance.is_from_oficial_chat(update):
            CommandCall.clima(user.username)

    except NotFoundError:
        update.message.reply_text(f"⚠️ Não consegui localizar a cidade "
                                  f"{text_location}!")
    except APICallError:
        update.message.reply_text(f"⚠️ Você precisa digitar uma cidade")


def config_handlers(instance: BotTelegramCore):
    logging.info('Psicografando satelites climaticos...')

    instance.add_handler(CommandHandler("clima", weather, pass_args=True))
