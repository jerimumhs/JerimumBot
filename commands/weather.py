import logging

import pyowm
from pyowm.exceptions.api_response_error import NotFoundError
from pyowm.exceptions.api_call_error import APICallError
from decouple import config
from telegram.ext import CommandHandler

from core import BotTelegramCore, throttle

logging.basicConfig(format='%(asctime)s - %(name)s - '
                           '%(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# @throttle()
def weather(bot, update, args):
    """Define weather at certain location"""
    api_key = config('OPENWEATHERMAP_TOKEN')
    owm = pyowm.OWM(api_key)
    text_location = " ".join(args)
    try:
        observation = owm.weather_at_place(text_location)
        weather = observation.get_weather()
        humidity = weather.get_humidity()
        wind = weather.get_wind()
        temp = weather.get_temperature('celsius')
        update.message.reply_text(f"🧭 Localização: {text_location}\n"
                                  f"🔥️ Temp. Maxima: "
                                  f"{temp.get('temp_max')} °C \n"
                                  f"❄️ Temp. Minima: "
                                  f"{temp.get('temp_min')} °C \n"
                                  f"💨 Vel. do Vento: "
                                  f"{wind.get('speed')} m/s \n"
                                  f"💧 Humidade: "
                                  f"{humidity}%")
    except NotFoundError:
        update.message.reply_text(f"⚠️ Não consegui localizar a cidade "
                                  f"{text_location}!")
    except APICallError:
        update.message.reply_text(f"⚠️ Você precisa digitar uma cidade")


def config_handlers(instance: BotTelegramCore):
    logging.info('Psicografando satelites climaticos...')

    instance.updater.dispatcher.\
        add_handler(CommandHandler("clima", weather, pass_args=True))
